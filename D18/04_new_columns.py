import pandas as pd

df = pd.DataFrame({
    "request_id": ["r1", "r2", "r3", "r4", "r5"],
    "model": ["gpt-4o", "claude-sonnet", "gemini-flash", "gpt-4o", "gemini-flash"],
    "prompt_tokens": [820, 640, 512, 1020, 300],
    "completion_tokens": [310, 255, 180, 402, 95],
    "latency_ms": [1450, 1210, 640, 1890, 410],
    "cost_usd": [0.0112, 0.0089, 0.0014, 0.0154, 0.0005],
})

df["total_tokens"] = df["prompt_tokens"] + df["completion_tokens"]
df["cost_per_1k_tokens"] = (df["cost_usd"] / df["total_tokens"] * 1000).round(5)
df["latency_sec"] = df["latency_ms"] / 1000
df["is_expensive"] = df["cost_usd"] > 0.01

print(df)