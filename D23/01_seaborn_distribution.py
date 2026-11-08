import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

rng = np.random.default_rng(42)
df = pd.DataFrame({
    "model": rng.choice(["GPT-4o", "Claude"], 200),
    "latency_ms": rng.normal(1000, 250, 200),
})

sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.histplot(data=df, x="latency_ms", hue="model", bins=20, ax=axes[0])
axes[0].set_title("Latency Histogram")
sns.kdeplot(data=df, x="latency_ms", hue="model", fill=True, ax=axes[1])
axes[1].set_title("Latency Density")
plt.tight_layout()
plt.show()