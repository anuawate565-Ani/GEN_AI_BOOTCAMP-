import matplotlib.pyplot as plt

ages = [ 30, 39, 44, 45, 67, 80, 90 , 99]

plt.hist(ages, bins=5, color= 'skyblue', edgecolor= 'black')

plt.title("AGES COMPARISON")
plt.xlabel("Ages")
plt.ylabel("Frequency")

plt.show()