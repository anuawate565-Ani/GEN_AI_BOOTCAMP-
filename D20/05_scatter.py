import matplotlib.pyplot as plt

training_sample = [ 100, 200, 300, 400, 500, 600, 701, 800, 900, 101]
acc = [65, 70, 72, 75, 78, 80,  85, 90, 95, 98]


plt.scatter(training_sample, acc, color='blue')

plt.title("ML model acc comparison")
plt.xlabel("Training Sample")
plt.ylabel("acccuracy")

plt.show()