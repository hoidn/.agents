"""Split a PDF into consecutive page ranges that each fit an upload size limit.

The Chrome extension's file_upload accepts at most 10.4 MB per call, so a
larger PDF is uploaded as several parts, one call each. The split is lossless:
pages are copied, never re-encoded. The source file is never modified.

Usage: python split_pdf.py SRC.pdf OUT_DIR [--max-mb 9.5]
Writes OUT_DIR/<stem>-pAAA-BBB.pdf and prints one path per line.
Depends on: pypdf.
"""

import argparse
import io
import logging
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter

DESCRIPTION = "Split a PDF into consecutive page ranges that each fit an upload size limit."
BYTES_PER_MB = 1_000_000

# A link to a page outside its part is dropped by design; pypdf warns once per page.
logging.getLogger("pypdf").setLevel(logging.ERROR)


def _pdf_bytes(reader: PdfReader, start: int, stop: int) -> bytes:
    """Return pages [start, stop) of reader as a standalone PDF."""
    writer = PdfWriter()
    writer.append(reader, pages=(start, stop))
    buffer = io.BytesIO()
    writer.write(buffer)
    return buffer.getvalue()


def plan_ranges(page_sizes: list[int], limit: int) -> list[tuple[int, int]]:
    """Pack consecutive pages greedily into ranges whose summed size is within limit.

    A page's standalone size is an upper bound on what it adds to a part
    (shared fonts are counted once per part), so each planned part fits.
    """
    ranges = []
    start, total = 0, 0

    for index, size in enumerate(page_sizes):
        if size > limit:
            raise ValueError(f"page {index + 1} alone is {size / BYTES_PER_MB:.1f} MB, over the limit")
        if total + size > limit:
            ranges.append((start, index))
            start, total = index, 0
        total += size

    ranges.append((start, len(page_sizes)))
    return ranges


def split(src: Path, out_dir: Path, limit: int) -> list[Path]:
    """Write the parts of src into out_dir and return their paths in page order."""
    reader = PdfReader(src)
    count = len(reader.pages)
    page_sizes = [len(_pdf_bytes(reader, i, i + 1)) for i in range(count)]

    paths = []
    for start, stop in plan_ranges(page_sizes, limit):
        data = _pdf_bytes(reader, start, stop)
        if len(data) > limit:
            raise ValueError(f"pages {start + 1}-{stop} came to {len(data) / BYTES_PER_MB:.1f} MB, over the limit")

        path = out_dir / f"{src.stem}-p{start + 1:03d}-{stop:03d}.pdf"
        path.write_bytes(data)
        paths.append(path)

    return paths


def main() -> int:
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("src", type=Path)
    parser.add_argument("out_dir", type=Path)
    parser.add_argument("--max-mb", type=float, default=9.5)
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    for path in split(args.src, args.out_dir, int(args.max_mb * BYTES_PER_MB)):
        print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
