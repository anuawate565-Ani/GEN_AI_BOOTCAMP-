import io

import pandas as pd

csv_data = """request_id,model,prompt_tokens,completion_tokens,latency_ms,cost_usd
r1,gpt-4o,820,310,1450,0.0112
r2,claude-sonnet,640,255,1210,0.0089
r3,gemini-flash,512,180,640,0.0014
r4,gpt-4o,1020,402,1890,0.0154
r5,gemini-flash,300,95,410,0.0005
"""

df = pd.read_csv(io.StringIO(csv_data))

print(df.head(3))
df.info()
print(df.describe())