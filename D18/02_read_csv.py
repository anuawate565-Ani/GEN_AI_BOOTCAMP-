import pandas as pd

df = pd.DataFrame({
    "request_id": ["r1", "r2", "r3", "r4", "r5"],
    "model": ["gpt-4o", "claude-sonnet", "gemini-flash", "gpt-4o", "gemini-flash"],
    "latency_ms": [1450, 1210, 640, 1890, 410],
    "cost_usd": [0.0112, 0.0089, 0.0014, 0.0154, 0.0005],
}).set_index("request_id")

print(df.loc["r2", ["model", "latency_ms"]])
print(df.iloc[0:3, 1:3])

slow_gpt_requests = df[(df["model"] == "gpt-4o") & (df["latency_ms"] > 1500)]
print(slow_gpt_requests)