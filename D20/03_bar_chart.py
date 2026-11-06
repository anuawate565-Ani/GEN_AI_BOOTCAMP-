import matplotlib.pyplot as plt

model = ["SVM", "XGBoost", "logistic regression", "Random Forest", "Decision Tree"]
acc = [56, 73, 66, 89 ,33]

plt.barh(model, acc, color='red')

plt.title("ML model acc comparison")
plt.xlabel("ML model")
plt.ylabel("acccuracy")

plt.show()