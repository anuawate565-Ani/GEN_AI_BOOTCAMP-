import matplotlib.pyplot as plt

income = [25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000]

plt.boxplot(income)

plt.title("Average imcome salary")
plt.ylabel("Anuual salary")

plt.show()