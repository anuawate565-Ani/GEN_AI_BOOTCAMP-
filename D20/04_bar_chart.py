import matplotlib.pyplot as plt

models = ["LogReg", "SVM", "RandomForest", "XGBoost", "LightGBM"]
accuracy = [0.84, 0.86, 0.89, 0.91, 0.90]
inference_ms = [3.2, 6.7, 12.5, 8.1, 5.4]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.bar(models, accuracy, color="steelblue")
ax1.set_title("Model Accuracy")
ax1.set_ylabel("Accuracy")
ax1.set_ylim(0.8, 0.95)

ax2.barh(models, inference_ms, color="coral")
ax2.set_title("Inference Time (ms)")
ax2.set_xlabel("Milliseconds")

plt.tight_layout()
plt.show()