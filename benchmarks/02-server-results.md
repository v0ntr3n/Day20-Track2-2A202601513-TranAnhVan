# 02 - Serve: load test + saturation reading

Host `Windows-AMD64` Â· llama.cpp `b10488` Â·
`--parallel 4` Â· `ctx=2048` Â· `threads=20` Â·
`ngl=99`

| Users | Reqs | RPS | P50 (ms) | P95 (ms) | P99 (ms) | Eff. concurrency | Failures |
|:--|--:|--:|--:|--:|--:|--:|--:|
| 10 | 315 | 5.34 | 880 | 1700 | 2700 | 5.3 | 0.0% |
| 50 | 349 | 5.92 | 7300 | 8300 | 9700 | 41.9 | 0.0% |

*Effective concurrency = RPS x average latency (Little's Law) -- how many requests were
really in flight, regardless of how many users locust simulated. It counts queued requests
too, so the occupancy/slot ratio can legitimately exceed 1.0; it is occupancy, not
utilisation. For true slot utilisation use the server's own gauges (`make metrics`).*

## What these two runs say

| Going from 10 to 50 users | |
|:--|--:|
| Offered load | 5x |
| Throughput actually delivered | **1.11x** (22% of linear) |
| P95 latency | **4.88x** |
| Effective concurrency at 50 users | 41.9 vs `--parallel 4` slots (occupancy/slot ratio 10.48) |

**Saturated.** Throughput delivered only 1.11x for 5x the offered load, and effective concurrency (41.9) is at or above all 4 decode slots. Saturation sets in somewhere at or below 50 users; the load you added beyond that point became queue time rather than throughput.

Throughput moved 1.11x while P95 moved 4.88x. That gap is the goodput argument: past saturation you buy throughput by spending latency, and if your SLO is a P95 target then the requests you added are no longer being served within it. (This lab does not fix an SLO number for you -- pick one in your write-up and state how much goodput you keep at it.)

## Reading

The server saturates at approximately 10-12 concurrent users. 

**Key Evidence:**
1. **RPS Plateau vs Latency Explosion:** Increasing offered load by 5x (10 to 50 users) increased delivered RPS by only 1.11x (5.34 to 5.92 req/s), while P95 response time ballooned by 4.88x from 1,700 ms to 8,300 ms.
2. **Effective Concurrency vs Slot Capacity:** At 50 users, Little's Law indicates an effective concurrency of 41.9 in-flight requests against `--parallel 4` active slots (occupancy ratio of 10.48x). 
3. **Metrics Gauge Proof:** Continuous metrics sampling (`make metrics`) showed peak active slots saturating at 3.87 / 4.0 slots, while the `llamacpp:requests_deferred` queue rose up to 43 queued requests.

The additional latency under 50 users is almost purely queuing delay in the server backlog. If enforcing a strict SLO of P95 â¤ 2,500 ms, goodput drops drastically above 10 users. To increase goodput@SLO, the primary knob to adjust first is increasing `--parallel` (e.g. from 4 to 8 or 16 slots), allowing continuous batching to decode more sequences concurrently across available VRAM capacity.
