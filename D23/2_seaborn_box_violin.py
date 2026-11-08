import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

rng = np.random.default_rng(42)
df = pd.DataFrame({
    "model": rng.choice(["LogReg", "SVM", "XGBoost"], 150),
    "accuracy": rng.uniform(0.75, 0.95, 150),
})

sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.boxplot(data=df, x="model", y="accuracy", ax=axes[0])
axes[0].set_title("Accuracy - Boxplot")
sns.violinplot(data=df, x="model", y="accuracy", ax=axes[1])
axes[1].set_title("Accuracy - Violin")
plt.tight_layout()
plt.show()