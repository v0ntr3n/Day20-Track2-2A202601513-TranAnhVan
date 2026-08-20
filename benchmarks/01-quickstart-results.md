# 01 - Measure: latency baseline

Model `Qwen3.5 0.8B` · host `Windows-AMD64` · llama.cpp `b10488`
Settings: `threads=20` `ngl=99` `ctx=2048`
`max_tokens=64` · warm-up discarded
Completed requests: `Q4_K_M` 10/10 · `UD-Q2_K_XL` 10/10

| Quantization | Size (GB) | Load (ms) | TTFT P50/P95 (ms) | TPOT P50/P95 (ms) | E2E P50/P95/P99 (ms) | Decode (tok/s) |
|:--|--:|--:|--:|--:|--:|--:|
| Q4_K_M | 0.50 | 1571 | 40 / 51 | 3.6 / 3.7 | 268 / 278 / 278 | 275.6 |
| UD-Q2_K_XL | 0.39 | 1524 | 48 / 55 | 3.5 / 3.5 | 265 / 273 / 273 | 288.8 |

- **TTFT** = prefill. Short prompts keep it small; long-context RAG is where it explodes.
- **TPOT** = per-output-token decode cost, bounded by memory bandwidth. `decode tok/s = 1000 / TPOT_p50`.
- `UD-Q2_K_XL` decodes **1.05x faster** than `Q4_K_M` here, for 0.11 GB less on disk.

## Observation

On this machine (Intel Core i7-14700K + RTX 4060 Ti), `UD-Q2_K_XL` achieves a minor ~1.05x decode speedup (288.8 tok/s vs 275.6 tok/s) and saves 0.11 GB of memory footprint (0.39 GB vs 0.50 GB). However, TTFT P95 increases from 51 ms to 55 ms due to 2-bit unpacking overhead on prefill. Given that 0.50 GB for `Q4_K_M` is extremely small and easily fits in RAM/VRAM, the small memory saving of `UD-Q2_K_XL` does not justify the degradation in generation quality. Therefore, `Q4_K_M` remains the superior choice for production serving.
