# Prose standards

Standards for the running text of a manuscript section, distilled from a referee's and an editor's reviews of
drafted Results text. This file is uploaded with the pack as it is. The first four blocks are **hard invariants**
(checked strictly where applicable); **Shape** states **style guidelines** (readability targets, not mechanical
pass/fail counters). The brief states which Results-specific rules apply to the target section.

## Numbers

- Every primary or comparative number in the text is printed in a figure or a table of the manuscript. A primary
  result that no figure or table shows is not stated; it is listed in the Notes as lacking a display item. Minor
  one-off control or sanity-check numbers (e.g., an interpolation or single-scan sensitivity check) may appear in
  running text when provided in the brief's Facts with recorded provenance.
- Running text carries anchor values: the value of the method and of its main comparator. For a group of
  methods it gives the range. Per-method values stay in the table that prints them.
- A ratio, factor or percentage is computed from printed values and given as its actual value or range.

## Claims

- A claim names its scope: the statistic, the metric and the data it holds for ("matches in median held-out
  phase error", not "matches").
- In Results, where the comparator does better, the text says so beside the claim: on how many cases, and the
  largest gap. In an Abstract or Introduction summary, keep caveats proportional to the passage length.
- A condition that differs between the methods compared is stated once, plainly: an input one method is
  given and another must estimate, a different training set or objective, runs that failed and were replaced,
  data left out.
- In Results, a cause is stated only where an experiment in the manuscript isolates it; otherwise the text states
  what was observed, and when two factors change together, says that they do. In Discussion, physical
  interpretation or hypotheses are permitted when framed explicitly as interpretation rather than established
  cause.
- A method or protocol is described to the extent that the manuscript's tables support, and not characterized
  beyond them.
- Description stands without hype, intensifiers or evaluative padding ("substantially", "dramatically", "severe",
  "clean", "actually"). Logical and scope-restricting words ("only", "even") remain permitted where they tighten
  precision or contrast.

## Terms and symbols

- The manuscript's defined terms are used exactly as it defines them; the text introduces no synonym for one.
- A symbol appears only where a reader arriving in reading order has already met its definition. Before that
  point the text uses words.

## Division of labour

- Results say what each stage does and why. Solver names, settings, iteration limits and other procedure stay
  in Methods.
- Each topic is argued in one subsection. Another subsection that touches it points there.
- The Introduction's framing is not repeated; a Results subsection opens with one sentence of orientation that
  states the scientific question or finding, not a procedural inventory.
- A cross-reference points to the item that shows the thing cited (a step number to the algorithm, not to a
  figure that prints no steps), and a sentence cites the fewest items that support it.

## Shape (style guidelines)

- Lead each Results subsection and paragraph with its scientific question or takeaway, and carry information
  forward from known context to new result.
- A paragraph does one job; aim for about 150 words at most.
- Keep sentences readable (aim for about 40 words at most). Put key contrasts in main clauses, avoid nested or
  chained parentheticals, and split a claim and its caveat into two clean sentences rather than compressing both
  into one parenthetical-heavy sentence.
- The length target for the passage is the one the brief gives.
