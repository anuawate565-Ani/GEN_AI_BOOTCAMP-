import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

rng = np.random.default_rng(42)
prompt_tokens = rng.integers(100, 2000, 200)
df = pd.DataFrame({
    "prompt_tokens": prompt_tokens,
    "latency_ms": prompt_tokens * 0.5 + rng.normal(0, 100, 200),
    "cost_usd": prompt_tokens * 0.00001 + rng.normal(0, 0.002, 200),
})

plt.figure(figsize=(7, 5))
sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()