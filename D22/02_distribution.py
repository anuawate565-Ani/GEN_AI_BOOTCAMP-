import matplotlib.pyplot as plt
import seaborn as sns

confidence = [45, 55, 60, 65, 70, 72, 75, 80, 85, 90, 92, 95, 98]

accuracy = [65, 70, 72, 75, 78, 80, 82, 85, 87, 90, 92, 95]

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.histplot(confidence, bins=5, ax=axes[0])

axes[0].set_title("Model Prediction Confidence")
axes[0].set_xlabel("Confidence (%)")
axes[0].set_ylabel("Frequency")

sns.kdeplot(accuracy, fill=True, ax=axes[1])

axes[1].set_title("Model Accuracy Distribution")
axes[1].set_xlabel("Accuracy (%)")
axes[1].set_ylabel("Density")

plt.tight_layout()
plt.show()