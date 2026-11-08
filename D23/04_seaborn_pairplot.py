import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

rng = np.random.default_rng(42)
df = pd.DataFrame({
    "model": rng.choice(["LogReg", "RandomForest"], 100),
    "accuracy": rng.uniform(0.75, 0.95, 100),
    "f1": rng.uniform(0.70, 0.93, 100),
})

sns.pairplot(df, hue="model", diag_kind="kde")
plt.show()