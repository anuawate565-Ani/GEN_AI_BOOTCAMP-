import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    "Study_Hours" : [2,3,4,5,6,7,8,9,10],
    "Pratice" : [10, 29, 33, 44, 54, 65, 78, 87, 90],
    "Attendence" : [50, 55, 54, 56, 59, 67, 87 ,88,98],
    "Sleep_Hours" : [8, 8, 4, 8, 5, 7, 9, 8, 7],
    "Exam_Score" : [50, 60, 70, 80, 90, 100, 110, 120, 130]
}

df = pd.DataFrame(data)
sns.pairplot(df)

plt.title("Pairplot of Features")
plt.show()