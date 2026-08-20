# 01 - Tune: thread-count sweep

Model `Qwen3.5-0.8B-Q4_K_M.gguf` Â· host `Windows-AMD64` Â· llama.cpp `b10488`
CPU: **20 physical Â· 28 logical** cores Â· `ngl=99` Â· metric `tg128`

| threads (-t) | tg128 (tok/s) | vs best |
|:--|--:|--:|
| 1 | 291.7 | 99% |
| 10 | 292.4 | 100% |
| 20 | 293.0 | 100% |
| 28 | 293.1 | 100% |
| 56 | 293.3 | 100% |

**Best**: `-t 56` at 293.3 tok/s
**Slowest tested**: `-t 1` at 291.7 tok/s (1.01x spread)
**Against the physical-core default** (`-t 20`, 293.0 tok/s): 1.00x

Use this in your run:

```bash
LAB_N_THREADS=56 make bench
```

## Explanation

On this system, the thread sweep yields an almost flat performance curve across thread counts (291.7 tok/s at -t 1 vs 293.3 tok/s at -t 56, a minor 1.005x spread). 

This behavior occurs because `ngl=99` offloads all 24 layers of Qwen3.5 0.8B to the NVIDIA GeForce RTX 4060 Ti GPU. Matrix multiplication for prefill and decode is executed entirely inside CUDA kernels on the GPU's tensor/CUDA cores. The host CPU threads are only responsible for kernel dispatch, prompt tokenization, and token sampling. Consequently, increasing host CPU thread count does not increase compute throughput, as performance is entirely memory-bandwidth bound on the GPU VRAM interface. When running GPU-offloaded inference, thread count allocation (`-t`) has minimal impact compared to CPU-only execution.
