# Bonus - GPU offload sweep

Host `Windows-AMD64` Â· backend(s) `nvidia_cuda, vulkan` Â·
llama.cpp `b10488` Â· `threads=20` Â· metric `tg128`

| -ngl | tg128 (tok/s) | vs -ngl 0 | vs best |
|:--|--:|--:|--:|
| 0 | 53.6 | 1.00x | 19% |
| 8 | 80.6 | 1.50x | 28% |
| 16 | 130.6 | 2.44x | 46% |
| 24 | 261.1 | 4.87x | 92% |
| 32 | 264.3 | 4.93x | 93% |
| 99 | 284.0 | 5.30x | 100% |

Best: `-ngl 99` at 284.0 tok/s
-- 5.30x faster than CPU-only.

Where the curve flattens tells you the model ran out of layers to move. Where it
*peaks below* full offload tells you something did not fit and the accelerator
started paying to fetch weights it could not hold.

## Finding

Full offload (`-ngl 99`) provides the highest throughput (284.0 tok/s), delivering a **5.30x speedup** compared to CPU-only execution (`-ngl 0` at 53.6 tok/s).

**Performance Knee & Transfer Bottlenecks:**
- Offloading 24 transformer layers (`-ngl 24`) achieves 261.1 tok/s (4.87x vs CPU), capturing 92% of maximum potential throughput.
- Offloading the remaining output norm and lm_head tensors (`-ngl 99`) provides the final jump to 284.0 tok/s because it eliminates PCIe transfer overhead for the final vocabulary projection.
- Since the RTX 4060 Ti has 16 GB VRAM and Qwen3.5 0.8B requires less than 1 GB VRAM, the model fits entirely inside VRAM. Partial offload (`-ngl < 24`) creates a hybrid pipeline where host-to-device transfers over PCIe become the primary bottleneck. Full offload eliminates inter-layer PCIe traffic entirely, allowing the GPU VRAM bandwidth (288 GB/s) to be fully utilized.
