import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    "Model" : ["SVM", "SVM", "RF", "RF", "XGB", "XGB", "LGM", "LGM"],
    "Accuracy" : [0.89, 0.66, 0.76, 0.73, 0.85, 0.67, 0.98, 0.88]

}

df = pd.DataFrame(data)

sns.barplot(data=df, x="Model", y="Accuracy")

plt.title("Model Accuracy Bar Plot")
plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.show()