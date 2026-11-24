# Build log — One Sentence for a Traveler from 1800

## What was built
`main.py` (Python stdlib only) writes one original sentence explaining the
modern internet to a traveler from 1800, to `/output/entry.txt`.
The sentence uses only images a person from 1800 could picture — a road,
a post office, a library, a letter, a book, a spoken word — and covers
two-way instant exchange: a message reaches any door before you finish a
breath, and an answer comes back just as fast.

## The sentence (191 characters, one sentence)
> Picture every post office and library on earth joined by one road, so any letter, book, or spoken word can reach any door before you finish a breath, and an answer can come back just as fast.

## Revision history (two distinct write/edit messages, separate commits)
1. First draft (135 chars): "Picture every post office and library on earth
   joined by one road, so any letter or book can reach any door before you
   finish a breath." — commit `2688a6a`.
2. Real second edit: added "spoken word" and the return journey — "and an
   answer can come back just as fast" — so the picture covers two-way
   instant exchange (letters, books, voices; an answer back), not just
   one-way delivery. Final text 191 chars — commit `20e4b35`.

## Verification
- Ran `python3 main.py` twice; both runs byte-identical (`cmp` passed).
- `sha256` of `/output/entry.txt`:
  `d7e47220b37958dfe62c0ce918a2818334225c9f6b0795f169aaeaa080189813`
- Character count: 191 (limit 200); byte count 191; one sentence (one period);
  no trailing newline; UTF-8, not only whitespace.
- `.makefun/owner.json`: exactly 57 bytes, no trailing newline.
- No other entry was read while writing this sentence; written from scratch.
