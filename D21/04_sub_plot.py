import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(11)
epochs = np.arange(1, 51)
train_acc = 1 - np.exp(-0.08 * epochs) + rng.normal(0, 0.01, 50)
val_acc = 1 - np.exp(-0.06 * epochs) + rng.normal(0, 0.015, 50)

fig, axes = plt.subplots(2, 2, figsize=(12, 9))

axes[0, 0].plot(epochs, train_acc, color="blue")
axes[0, 0].set_title("Training Accuracy")

axes[0, 1].plot(epochs, val_acc, color="orange")
axes[0, 1].set_title("Validation Accuracy")

axes[1, 0].hist(train_acc - val_acc, bins=15, color="purple")
axes[1, 0].set_title("Generalization Gap")

axes[1, 1].scatter(train_acc, val_acc, alpha=0.6)
axes[1, 1].set_title("Train vs Val Accuracy")

for ax in axes.flat:
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()