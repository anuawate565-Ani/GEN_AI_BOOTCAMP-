import matplotlib.pyplot as plt
import numpy as np

models = ["LogReg", "SVM", "RandomForest", "XGBoost", "LightGBM"]
datasets = ["Reviews", "Support", "Legal", "Medical"]

rng = np.random.default_rng(21)
f1_matrix = rng.uniform(0.70, 0.95, size=(len(models), len(datasets)))

fig, ax = plt.subplots(figsize=(8, 6))
image = ax.imshow(f1_matrix, cmap="YlGnBu", aspect="auto")
plt.colorbar(image, ax=ax, label="F1 Score")

ax.set_xticks(np.arange(len(datasets)), labels=datasets)
ax.set_yticks(np.arange(len(models)), labels=models)

for i in range(len(models)):
    for j in range(len(datasets)):
        ax.text(j, i, f"{f1_matrix[i, j]:.2f}", ha="center", va="center", color="black")

ax.set_title("F1 Score by Model and Dataset")
plt.tight_layout()
plt.show()