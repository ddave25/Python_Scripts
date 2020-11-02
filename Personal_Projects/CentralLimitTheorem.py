import random
import matplotlib.pyplot as plt

Sample_mean_array = []

for i in range(100000):
    Y = 0

    for N in range(10000):
        X_n = random.random()
        Y += X_n

    Sample_mean_array.append(Y/10000)

# An "interface" to matplotlib.axes.Axes.hist() method
n, bins, patches = plt.hist(x=Sample_mean_array, bins='auto', alpha=0.7, rwidth=0.85)

plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
