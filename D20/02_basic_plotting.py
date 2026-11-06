import matplotlib.pyplot as plt
import numpy as np

epochs = np.arange(1, 21)
train_loss = np.exp(-0.25 * epochs) + np.random.normal(0, 0.02, 20)
val_loss = np.exp(-0.2 * epochs) + np.random.normal(0, 0.03, 20)

plt.figure(figsize=(8, 5))
plt.plot(epochs, train_loss, marker="o", label="Train Loss")
plt.plot(epochs, val_loss, marker="s", label="Validation Loss")
plt.title("Training vs Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()