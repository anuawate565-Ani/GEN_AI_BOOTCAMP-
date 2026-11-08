import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Exam_Score": [35, 40, 50, 55, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

sns.regplot(
    data=df,
    x="Study_Hours",
    y="Exam_Score"
)

plt.title("Study Hours vs Exam Score")
plt.show()