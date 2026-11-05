import pandas as pd

df = pd.DataFrame({
    "request_id": ["r1", "r2", "r3", "r4", "r5"],
    "model": ["gpt-4o", "claude-sonnet", "gemini-flash", "gpt-4o", "gemini-flash"],
    "prompt_tokens": [820, 640, 512, 1020, 300],
    "latency_ms": [1450, 1210, 640, 1890, 410],
})

df["latency_tier"] = df["latency_ms"].apply(
    lambda ms: "fast" if ms < 800 else "medium" if ms < 1500 else "slow"
)

df["prompt_size"] = df["prompt_tokens"].apply(
    lambda tokens: "large" if tokens > 800 else "small"
)

df["model_provider"] = df["model"].apply(
    lambda name: name.split("-")[0]
)

df["latency_per_token"] = df.apply(
    lambda row: round(row["latency_ms"] / row["prompt_tokens"], 3), axis=1
)

print(df)