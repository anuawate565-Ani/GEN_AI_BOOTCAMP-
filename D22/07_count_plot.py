import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    "Result" : ["Pass", "Fail", "Pass", "Pass", "Fail", "Pass", "Fail", "Pass", "Fail", "Pass"]

}

df = pd.DataFrame(data)

sns.countplot(data=df, x="Result")

plt.title("Student Result Count Plot")
plt.xlabel("Result")
plt.ylabel("Count")
plt.show()