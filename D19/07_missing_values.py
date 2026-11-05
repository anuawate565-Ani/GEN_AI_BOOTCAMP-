import numpy as np
import pandas as pd

ml_results = pd.DataFrame({
    "run_id": ["run_01", "run_02", "run_03", "run_04", "run_05"],
    "model_name": ["LogisticRegression", "RandomForest", "XGBoost", "SVM", "XGBoost"],
    "accuracy": [0.84, 0.89, np.nan, 0.85, 0.93],
    "f1": [0.80, np.nan, 0.895, 0.84, 0.91],
    "train_time_sec": [2.1, 15.4, np.nan, 22.0, 11.2],
})

print(ml_results.isnull().sum())

filled_df = ml_results.copy()
filled_df["f1"] = filled_df["f1"].fillna(filled_df["f1"].mean())
filled_df["train_time_sec"] = filled_df["train_time_sec"].fillna(filled_df["train_time_sec"].median())
print(filled_df)

clean_df = ml_results.dropna(subset=["accuracy"])
print(clean_df)