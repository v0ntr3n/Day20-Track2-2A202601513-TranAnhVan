# 03 - Integrate: RAG pipeline run

Host `Windows-AMD64` · llama.cpp `b10488` ·
retrieval backend: **keyword overlap** · 3 queries

| Query | Contexts retrieved | embed (ms) | retrieve (ms) | llm (ms) | total (ms) |
|:--|--:|--:|--:|--:|--:|
| Why is goodput more useful than raw throughp... | goodput, paged, radix | 0.0 | 0.0 | 2903.3 | 2903.4 |
| What problem does PagedAttention actually so... | paged, radix, disagg | 0.0 | 0.0 | 2382.4 | 2382.5 |
| When does splitting prefill and decode help?... | disagg, radix, batching | 0.0 | 0.0 | 2662.7 | 2662.7 |

Mean per stage (ms): embed **0.0** Â· retrieve **0.0** Â·
llm **2649.5** Â· total **2649.5**
Dominant stage: **llm** (100% of total)

## Answers returned

**Why is goodput more useful than raw throughput?**

> Based on the provided context, **Goodput** is more useful than raw throughput because it focuses on **SLO (Service Level Objective) compliance** rather than just raw data volume.

The context explicitly states that:
1.  **Goodput** counts only requests per second that met the TTFT and TPOT targets.
2.  **Throughput at saturation** ignores SLOs.

Therefore, Goodput is useful because it ensures that

**What problem does PagedAttention actually solve?**

> PagedAttention solves the problem of **internal fragmentation in GPU memory** by storing the Key-Value (KV) cache in non-contiguous pages.

This is achieved by removing the internal fragmentation that would otherwise waste most GPU memory.

**When does splitting prefill and decode help?**

> Splitting prefill and decode helps when **prefill is compute-bound and decode is memory-bound**.

This is because the context explicitly states that "Disaggregated serving splits prefill and decode onto separate pools because prefill is compute-bound and decode is memory-bandwidth-bound." By separating these operations, the system can utilize different hardware resources (like compute vs. memory) 


## Real vs Stubbed Components

- **N16 Cloud/IaC:** Stubbed (local deployment)
- **N17 Data pipeline:** Stubbed (in-memory static documents)
- **N18 Lakehouse:** Stubbed (no delta storage)
- **N19 Vector + features:** Stubbed (keyword overlap matching, latency = 0.0 ms)
- **N20 Model Serving:** Real (`llama-server` on port 8080 serving OpenAI-compatible API)

**Latency & Bottleneck Reflection:**
The LLM generation stage accounts for 100% of total pipeline latency (2649.5 ms mean out of 2649.5 ms total). This matches expectation: local keyword retrieval operates in microsecond timeframes on small corpora, whereas LLM decode requires multi-step auto-regressive forward passes over KV cache. 

To halve the overall pipeline latency, we must attack the **LLM generation stage**. Actionable optimizations include:
1. **Speculative Decoding / Spec-decode:** Generate draft tokens via a small speculative model or MTP head to generate multiple tokens per forward pass.
2. **Output Token Limits:** Restrict max response tokens or trim prompt context length to minimize prefill and decode execution overhead.
