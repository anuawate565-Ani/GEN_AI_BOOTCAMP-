import pandas as pd

df = pd.DataFrame({
    "model": ["gpt-4o", "claude-sonnet", "gemini-flash", "gpt-4o", "gemini-flash", "claude-sonnet"],
    "prompt_tokens": [820, 640, 512, 1020, 300, 700],
    "completion_tokens": [310, 255, 180, 402, 95, 280],
    "latency_ms": [1450, 1210, 640, 1890, 410, 1100],
    "cost_usd": [0.0112, 0.0089, 0.0014, 0.0154, 0.0005, 0.0095],
})

usage_summary = (
    df.groupby("model")
    .agg(
        total_requests=("model", "count"),
        avg_latency_ms=("latency_ms", "mean"),
        total_cost_usd=("cost_usd", "sum"),
        max_prompt_tokens=("prompt_tokens", "max"),
    )
    .round(4)
    .sort_values("total_cost_usd", ascending=False)
)

print(usage_summary)