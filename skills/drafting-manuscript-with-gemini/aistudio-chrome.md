# AI Studio in Chrome: sending a pack and retrieving the reply

Mechanics for steps 4 and 5 of `SKILL.md`, verified on 2026-11-23 against `aistudio.google.com` with the
Claude in Chrome extension. The page is an Angular app; if a selector below stops matching, inspect the page
(`find`, a screenshot) and correct this file.

## Tools

Load in one `ToolSearch` call: `tabs_context_mcp`, `tabs_create_mcp`, `navigate`, `computer`, `find`,
`file_upload`, `javascript_tool`, `browser_batch`. Batch every predictable sequence with `browser_batch`.

## Facts that shape the procedure

| Fact | What to do |
|---|---|
| `file_upload` takes at most 10.4 MB per call and only staged files | one call per file; split a larger PDF with `scripts/split_pdf.py` |
| Enter sends the prompt (Shift+Enter is a new line) | type one line with no newline; long content goes in `brief.md` |
| The first click on the prompt box may not focus it | confirm the textarea's value with the status snippet before sending |
| Cmd+Enter did not send | click the Run button |
| `javascript_tool` output is cut at about 1,000 characters | return text in slices of 900 |
| Rendered reply text loses LaTeX; code blocks are verbatim | read `ms-code-block pre code` only |
| Turns far off screen are emptied | `scrollIntoView()` the turn before reading it |
| A chat with large attachments shows a spinner for 10 s or more | wait until `ms-chat-turn` elements exist |
| Run settings (thinking level, grounding) persist to later chats | read and report them; change them only on the user's word |
| `get_page_text` returns the whole chat with all controls | not for retrieval; use the snippets |

## Model

`https://aistudio.google.com/prompts/new_chat?model=<id>` opens a new chat with the model selected.

| Model | id |
|---|---|
| Gemini 4 Carbon (default) | `gemini-4-carbon` |
| Gemini 4 Argon | `gemini-4-argon` |
| Gemini 4 Neon | `gemini-4-neon` |
| Gemini 4 Hydrogen | `gemini-4-hydrogen` |

## Procedure

1. `tabs_context_mcp`, then a new tab, then `navigate` to the new-chat URL. Wait 3 s.
2. Run the status snippet. Stop if the page is not signed in or `model` is not the one asked for.
3. `find` "hidden file input (input type=file)" gives the input's ref. Call `file_upload` once per staged
   file with that ref. Never click "Upload files": it opens a native picker you cannot operate.
4. Run the status snippet: `files` lists every staged file by name with a token count.
5. Click the prompt box by coordinate, `type` the one-line prompt, run the status snippet, and compare
   `prompt` with what you typed.
6. Click the Run button (`find` "Run button"). After 2 s the status snippet shows `generating: true`.
7. Wait in batches (`computer` `wait`, 10 s at most per action) and poll the status snippet until
   `generating` is false. `url` has changed to `/prompts/<id>`: record it.
8. Run the stash snippet. `role` is `Model` and `drafts` is 1. If `drafts` is 0 the reply is incomplete
   or off contract: ask in the same chat for the block again, complete, ending with the sentinel line.
9. Read `window.__draft.slice(0, 900)`, `slice(900, 1800)` and so on until `chars` is covered, several
   slices per batch. Write the concatenation to `reply.tex` beside `pack/`.
10. Compare hashes. On a mismatch, read the slices again with a different width (800) and compare line by
    line; do not proceed with an unverified copy.
11. Read `window.__notes` in slices for Gemini's Notes. It needs no hash.

A revision in the same chat repeats steps 5 to 11; attach a further file with step 3 when the message is
long.

## Snippets

Status:

```js
const b = document.querySelector('ms-run-button button');
JSON.stringify({
  url: location.href,
  model: document.querySelector('ms-model-selector')?.innerText.split('\n')[1],
  thinking: document.querySelector('[role=combobox][aria-label="Thinking Level"]')?.innerText.trim(),
  grounding: document.querySelector('button[role=switch][aria-label="Grounding with Google Search"]')?.getAttribute('aria-checked'),
  files: [...document.querySelectorAll('ms-prompt-box ms-prompt-media')].map(e => e.innerText.split('\n').slice(1, 3).join(' ')),
  prompt: document.querySelector('textarea[aria-label="Enter a prompt"]')?.value,
  generating: /Stop/.test(b?.innerText ?? ''),
  turns: document.querySelectorAll('ms-chat-turn').length,
})
```

Stash the last turn's draft blocks (the code blocks that end with the sentinel) and hash them; `__notes` is
the whole turn's rendered text, the Notes included:

```js
const t = [...document.querySelectorAll('ms-chat-turn')].pop();
t.scrollIntoView();
await new Promise(r => setTimeout(r, 1500));
const blocks = [...t.querySelectorAll('ms-code-block pre code')].map(c => c.textContent.trim());
const drafts = blocks.filter(b => b.endsWith('% END OF DRAFT'));
window.__draft = drafts.join('\n\n');
window.__notes = t.innerText;
const h = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(window.__draft));
JSON.stringify({
  role: t.querySelector('[data-turn-role]')?.getAttribute('data-turn-role'),
  blocks: blocks.length,
  drafts: drafts.length,
  chars: window.__draft.length,
  notesChars: window.__notes.length,
  sha256: [...new Uint8Array(h)].map(x => x.toString(16).padStart(2, '0')).join(''),
})
```

Local hash of the saved reply, to compare with `sha256` above:

```bash
python -c "import hashlib, pathlib, sys; print(hashlib.sha256(pathlib.Path(sys.argv[1]).read_text().strip().encode()).hexdigest())" reply.tex
```

Change a run setting, only when the user asked (thinking level shown; the grounding switch takes `.click()`):

```js
const sel = document.querySelector('[role=combobox][aria-label="Thinking Level"]');
sel.click();
await new Promise(r => setTimeout(r, 600));
[...document.querySelectorAll('[role=option]')].find(o => o.innerText.trim() === 'High')?.click();
await new Promise(r => setTimeout(r, 600));
sel.innerText.trim()
```

## When the browser does not cooperate

After two or three failed attempts at one step (no response from the extension, a control that does not
react, a page that does not load), stop and tell the user what was tried. Do not switch to another route
to AI Studio, such as the API or a different browser, without asking.
