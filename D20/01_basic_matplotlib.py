import matplotlib.pyplot as plt

epochs = [1, 2, 3, 4, 5, 6]
loss = [ 0.3, 0.35, 0.38, 0.40, 0.43 , 0.44]

plt.plot(epochs, loss)

plt.title("Model loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")

plt.show()