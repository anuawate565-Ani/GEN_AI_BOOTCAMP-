# 04_histogram.py
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(7)
response_tokens = np.concatenate([
    rng.normal(250, 60, 800),
    rng.normal(600, 120, 200),
])

plt.figure(figsize=(8, 5))
plt.hist(response_tokens, bins=40, color="mediumseagreen", edgecolor="black")
plt.axvline(response_tokens.mean(), color="red", linestyle="--", label="Mean")
plt.title("Distribution of LLM Response Tokens")
plt.xlabel("Response Tokens")
plt.ylabel("Frequency")
plt.legend()
plt.show()