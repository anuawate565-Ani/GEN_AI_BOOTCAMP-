import matplotlib.pyplot as plt
import seaborn as sns

accuracy = [65, 70, 72, 75, 78, 80, 82, 85, 87, 90, 92, 95]

sns.kdeplot(accuracy, fill=True)

plt.title("Model Accuracy Distribution")
plt.xlabel("Accuracy (%)")
plt.ylabel("Density")

plt.show()