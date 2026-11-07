import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(3)
latency_data = {
    "GPT-4o": rng.normal(1400, 250, 100),
    "Claude": rng.normal(1200, 200, 100),
    "Gemini": rng.normal(650, 120, 100),
    "Llama-Local": rng.normal(900, 400, 100),
}

fig, ax = plt.subplots(figsize=(9, 6))
ax.boxplot(latency_data.values(), tick_labels=latency_data.keys(), patch_artist=True)
ax.set_title("API Latency Distribution by Model")
ax.set_ylabel("Latency (ms)")
ax.grid(axis="y", alpha=0.3)
plt.show()