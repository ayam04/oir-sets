# SSB OIR practice sets — free archive

Every OIR (Officer Intelligence Rating) test PDF I could find that is **actually free and directly downloadable** as of 2026-11-22, collected in one folder.

Stage 1 of the SSB/AFSB interview starts with the OIR. Boards hand out numbered **DIPR** booklets (set 34, 52, 74…) and candidates report which ones appeared. Those exact numbered booklets are *not* freely downloadable — see [what's missing](#whats-missing-the-numbered-dipr-booklets) below. What is here is the practice material that is open.

---

## contents

| file | pages | what it is | source |
|---|---|---|---|
| `files/defenceguru-oir-test-sets.pdf` | 23 | largest compilation here, ~170 figures, multiple sets back to back | Defence Guru |
| `files/defenceguru-practice-set-01.pdf` | 5 | practice set 1 | Defence Guru |
| `files/defenceguru-practice-set-02.pdf` | 5 | practice set 2 | Defence Guru |
| `files/defenceguru-practice-set-03.pdf` | 6 | practice set 3 | Defence Guru |
| `files/nimbus-oir-01.pdf` | 5 | OIR – 01 | Nimbus Defence Academy |
| `files/nimbus-oir-02.pdf` | 5 | OIR – 02 | Nimbus Defence Academy |
| `files/nimbus-oir-03.pdf` | 4 | OIR – 03 | Nimbus Defence Academy |
| `files/warriors-oir-sample-2025.pdf` | 5 | "OIR Test Series 2" with answers | Warriors Defence Academy |
| `files/oir-test-teachmint.pdf` | 9 | practice handout; text layer is garbled/mis-encoded, check page by page | Teachmint public assignment |

**9 files, 67 pages, ~8.6 MB.**

All verified as real PDFs with working page trees (`scripts/verify.py`).

Caveat on `oir-test-teachmint.pdf`: the embedded text is broken and it may be printed as images of uneven quality. Everything else extracts cleanly.

### not included
- `dipr-oir-blog.pdf` — turned out to be a 3-page printout of a blog article about DIPR, no questions.
- `defenceguru-officer-intelligence-rating.pdf` — 2-page advert with a phone number.
- Colonel Vyas's "[FREE PDF] OIR Practice Set 1" — it is 25 questions inline on a blog post, with several answers visibly wrong in the comments. No PDF file behind it.

---

## what's missing: the numbered DIPR booklets

The sets people trade in Telegram/Reddit circles (`34`, `35`, `52`, `53`, `54`, `55`, `74`, `75`, `93`, `100`, `101`, `168`–`170`, and now `197`, `198`, `202`, `203`) are genuine DIPR-designed booklets, numbered by DIPR to identify them. They leak out of the printing press, and they are **not** on any open host.

As of this writing they sit behind:

- `https://www.scribd.com/document/1004469581` — "Dipr Oir 34 35 53 54 73 74 Combined" (closest single source to a full set)
- `https://www.scribd.com/document/850857083` — "Original Oir Sets Dipr Booklet Number 34, 55, 53, 74"
- `https://www.scribd.com/document/804096008` — "DIPR BOOKLET 34"
- `https://www.scribd.com/document/818274803` — "DIPR-52-ssb-allahabad-bhopal-Bengaluru"
- Telegram `@ssbgeneraldiscussion` (31K subs) — posts board reports daily and sells the OIR set pack via WhatsApp. The channel's own ad confirms it holds them.

Scribd serves these behind a paywall/anti-bot wall, so they could not be pulled into this archive.

---

## which sets show up where

Community-reported only — self-selected candidates posting what they were given, not board statistics. Two separate snapshots from the public `@ssbgeneraldiscussion` channel disagree with each other month to month, which is itself the useful signal: **sets rotate, and boards reuse a small pool.**

**Newer snapshot (Nov 2026 reports):**

| board | sets reported |
|---|---|
| 1 AFSB Dehradun | 54, 52 |
| 3 AFSB Gandhinagar | 74, 75 |
| 4 AFSB Varanasi | 54, 55 |
| 5 AFSB Guwahati | 34, 35 |
| 11 SSB Prayagraj | 34, 74 |
| 12 SSB Bangalore | 35, 54, 93, 101 |
| 14 SSB Prayagraj | 93, 101 |
| 17 SSB Bangalore | 34, 52 |
| 18 SSB Prayagraj | 34, 52 / 52, 55 |
| 19 SSB Prayagraj | 197, 198 |
| 20 SSB Bhopal | 34, 35, 169, 170 |
| 21 SSB Bhopal | 54, 55 |
| 22 SSB Bhopal | 55, 75 |
| 24 SSB Bangalore | 34, 74 |
| 31 SSB Jalandhar | 202, 203 |
| 32 SSB Jalandhar | 35, 52, 53, 168, 170 |
| 33 SSB Bhopal | 53, 54 |
| 34 SSB Prayagraj | 52, 55 |
| NSB Kolkata | 34, 35, 55, 75 |
| NSB Vizag | 53, 74 |

Most repeated across all reports: **34 & 35**, then **52 & 53**, then **74 & 75**, then **54 & 55**. Practice in that order and you cover the overwhelming majority of reports.

Note the numbering is not static — `197/198` and `202/203` are now in circulation, above the `168–170` block that dominated 2025–26. Any list you see with a ceiling of 170 is already stale.

---

## how this was collected

`scripts/fetch.py` downloads from `scripts/urls.json`; `scripts/verify.py` re-checks every file as a valid PDF and reports pages, image count and extractable text. Re-run `fetch.py` to refresh — it skips files already present.

```
python scripts/fetch.py
python scripts/verify.py
```

---

## rights

These are third-party coaching-institute materials, redistributed for personal exam practice, with source credited per file. No ownership is claimed. If you hold rights to any file and want it removed, open an issue and it goes.

The DIPR booklets are Government of India test material and are **not** included here.
