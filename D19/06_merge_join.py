import pandas as pd

usage_df = pd.DataFrame({
    "request_id": ["r1", "r2", "r3", "r4", "r5"],
    "model_name": ["gpt-4o", "claude-sonnet", "gemini-flash", "gpt-4o", "llama-3-local"],
    "total_tokens": [1130, 895, 692, 1422, 395],
})

pricing_df = pd.DataFrame({
    "model_name": ["gpt-4o", "claude-sonnet", "gemini-flash"],
    "price_per_1k_tokens": [0.010, 0.007, 0.0008],
    "provider": ["OpenAI", "Anthropic", "Google"],
})

merged_df = usage_df.merge(pricing_df, on="model_name", how="left")
merged_df["estimated_cost_usd"] = (merged_df["total_tokens"] / 1000 * merged_df["price_per_1k_tokens"]).round(5)

print(merged_df)
print(merged_df[merged_df["provider"].isnull()])