import pandas as pd

model_results = {
    "model": ["LogReg", "RandomForest", "XGBoost", "SVM"],
    "accuracy": [0.82, 0.89, 0.91, 0.85],
    "train_time_sec": [2.1, 15.4, 9.8, 22.0],
}

df = pd.DataFrame(model_results)
accuracy_series = df["accuracy"]

print(df)
print(accuracy_series)
print(accuracy_series.index)
print(df.shape)