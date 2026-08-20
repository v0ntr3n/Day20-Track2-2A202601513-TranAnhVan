# Screenshots

**5 required.** All five come from the core path â none need bonus work, a GPU, or a
compiler. `make verify` counts files here and fails below 5.

Filenames are suggestions; the grader maps them via your REFLECTION. Keep the numbering
so they sort in run order.

## Required

| # | File | Command | Must show |
|---|---|---|---|
| 1 | `01-hardware-probe.png` | `make probe` | CPU, cores, RAM, accelerator, chosen llama.cpp build |
| 2 | `02-bench.png` | `make bench` | The results table â both quantizations, TTFT and TPOT columns |
| 3 | `03-serve-and-smoke.png` | `make serve` + `make smoke` | Server listening **and** a completion **and** non-zero `llamacpp:tokens_predicted_total` (rubric items 6 **and** 7 in one shot) |
| 4 | `04-locust-10.png` | `make load-10` | Locust summary: request count, RPS, and the 50%/95%/99% columns |
| 5 | `05-locust-50.png` | `make load-50` | Same, at 50 users |

For #3 you can either split the terminal or take two shots named `03a-` and `03b-` â
both count as one item.

## Optional (support your writeup; no extra points on their own)

| File | Command |
|---|---|
| `06-tune.png` | `make tune` â the thread curve behind REFLECTION Â§5 |
| `07-batching.png` | `make metrics` â peak `n_busy_slots_per_decode` under load |
| `08-pipeline.png` | `make pipeline` â contexts, timings, answers |
| `09-bonus.png` | any `benchmarks/bonus-*.md` table you produced |

## Tips

- **Crop tight.** Full-screen desktop shots get rejected. Show the data, not your wallpaper.
- Dark or light terminal is fine â just make sure the text is legible when zoomed.
- For locust, include the `Type Â· Name Â· # reqs Â· Median Â· 95%ile Â· 99%ile` row. That row
  *is* the evidence for item 8.
- PNG or JPG. Keep each under ~2 MB so your repo stays quick to clone.
- Take #3 **after** `make smoke` has actually printed the metrics delta â a screenshot of
  a server sitting idle does not show item 6.
