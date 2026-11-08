import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    "Model": ["SVM"] * 5 + ["RF"] * 5 + ["XGB"] * 5, 
    "Accuracy" : [
        0.98, 0.45, 0.67, 0.99, 0.88,
        0.98, 0.78, 0.71, 0.67, 0.55,
        0.59, 0.68, 0.34, 0.66, 0.77
    ]
}

df = pd.DataFrame(data)

sns.boxplot(data=df, x="Model", y="Accuracy")

plt.title("Model Accuracy Distribution")
plt.xlabel("ML Models")
plt.ylabel("Accuracy")
plt.show()