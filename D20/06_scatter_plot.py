import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)
prompt_tokens = rng.integers(100, 2000, 150)
latency_ms = 0.8 * prompt_tokens + rng.normal(0, 150, 150)
cost_usd = prompt_tokens * 0.00001 + rng.normal(0, 0.001, 150)

plt.figure(figsize=(8, 6))
scatter = plt.scatter(prompt_tokens, latency_ms, c=cost_usd, cmap="viridis", s=50, alpha=0.7)
plt.colorbar(scatter, label="Cost (USD)")
plt.title("Prompt Tokens vs Latency")
plt.xlabel("Prompt Tokens")
plt.ylabel("Latency (ms)")
plt.show()