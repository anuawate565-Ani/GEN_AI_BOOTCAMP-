import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

rng = np.random.default_rng(42)
prompt_tokens = rng.integers(100, 2000, 150)
df = pd.DataFrame({
    "prompt_tokens": prompt_tokens,
    "latency_ms": prompt_tokens * 0.5 + rng.normal(0, 80, 150),
})

plt.figure(figsize=(8, 6))
sns.regplot(data=df, x="prompt_tokens", y="latency_ms", ci=95, line_kws={"color": "purple"})
plt.title("Prompt Tokens vs Latency")
plt.xlabel("Prompt Tokens")
plt.ylabel("Latency (ms)")
plt.show()