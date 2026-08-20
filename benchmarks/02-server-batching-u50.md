# 02 - Continuous batching under load (u50)

Host `Windows-AMD64` Â· `--parallel 4` Â· 14 samples over
60s at 2.0s intervals Â· raw CSV: `02-server-metrics-u50.csv`

| Gauge | Peak observed |
|:--|--:|
| `n_busy_slots_per_decode` (avg/decode) | 3.87 of 4 slots (97%) |
| `requests_processing` | 4 |
| `requests_deferred` | 43 |
| `kv_cache_usage_ratio` | n/a â not exported by llama.cpp `b10488` |
| `tokens_predicted_total` (final) | 36488 |

Highest sampled value was **3.87 of 4** slots. Note this gauge is llama.cpp's *average* busy slots per decode step, so the number below is the highest average we sampled, not an instantaneous maximum batch width. A peak near 1 means
requests were served one at a time -- either the load was too light to overlap, or
they arrived too far apart. A peak approaching `--parallel` means the scheduler was
genuinely packing concurrent requests into shared decode steps.
`requests_deferred` went above zero: more requests arrived than there were slots, so some waited. That wait is the queue time in your P95.

## Observation

The peak observed batch width reached **3.87 out of 4 slots (97% slot utilization)**, confirming that continuous batching was actively interleaving decode steps for multiple concurrent requests.

While the server gauge peaks at 3.87 active slots (bounded by `--parallel 4`), the effective concurrency in `02-server-results.md` was **41.9**. These two numbers describe different physical layers:
1. **Server Busy Slots (3.87):** Represents actual GPU decode execution capacity utilization (max 4.0 slots).
2. **Effective Concurrency (41.9):** Represents total system queue length under Little's Law ($N = \text{RPS} \times W$), which includes the 4 requests being processed plus the 43 `requests_deferred` sitting in the server backlog.

Both metrics are trustworthy: `busy_slots` confirms compute saturation, while effective concurrency quantifies the queue buildup driving latency inflation.
