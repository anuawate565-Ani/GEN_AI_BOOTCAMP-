import matplotlib.pyplot as plt

epochs = [1, 2, 3, 4, 5]

train_accuracy = [60, 65, 72, 80, 90]
train_loss = [0.9, 0.7, 0.5, 0.3, 0.1]

val_accuracy = [55, 62, 68, 75, 82]
val_loss = [1.0, 0.8, 0.6, 0.5, 0.4]

fig, ax = plt.subplots(2, 2)

ax[0, 0].plot(epochs, train_accuracy)
ax[0, 0].set_title("Training Accuracy")

ax[0, 1].plot(epochs, train_loss)
ax[0, 1].set_title("Training Loss")

ax[1, 0].plot(epochs, val_accuracy)
ax[1, 0].set_title("Validation Accuracy")

ax[1, 1].plot(epochs, val_loss)
ax[1, 1].set_title("Validation Loss")

plt.tight_layout()
plt.show()