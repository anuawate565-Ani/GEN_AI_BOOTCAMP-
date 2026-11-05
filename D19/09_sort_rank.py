import pandas as pd

ml_results = pd.DataFrame({
    "run_id": ["run_01", "run_02", "run_03", "run_04", "run_05", "run_06"],
    "model_name": ["LogisticRegression", "RandomForest", "XGBoost", "SVM", "XGBoost", "RandomForest"],
    "accuracy": [0.84, 0.89, 0.91, 0.85, 0.93, 0.89],
    "inference_ms": [3.2, 12.5, 8.1, 6.7, 8.4, 13.1],
})

sorted_by_accuracy = ml_results.sort_values("accuracy", ascending=False)
print(sorted_by_accuracy)

ml_results["accuracy_rank"] = ml_results["accuracy"].rank(ascending=False, method="min").astype(int)
ml_results["speed_rank"] = ml_results["inference_ms"].rank(ascending=True, method="min").astype(int)

ranked_multi = ml_results.sort_values(["accuracy_rank", "speed_rank"])
print(ranked_multi)