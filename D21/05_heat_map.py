import matplotlib.pyplot as plt
import numpy as np

performance = np.array([[90, 85, 56],
                       [88, 89, 86],
                       [98, 67, 87]])

plt.imshow(performance, cmap= 'viridis')

plt.colorbar(label='Performance (%)')

plt.xticks(ticks=[0, 1, 2], labels=['SVM', 'XGBoost', 'Random Forest'])
plt.yticks(ticks=[0, 1, 2], labels=['Dataset A', 'Dataset B', 'Dataset C'])
plt.title("Model Performance Heatmap")
plt.xlabel("Model")
plt.ylabel("Dataset")

plt.show()