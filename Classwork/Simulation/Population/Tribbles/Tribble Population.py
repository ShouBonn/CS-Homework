from random import random, triangular
import matplotlib.pyplot as plt
import math

population = 1
day = 10
birth_rate = 0.15
death_rate = 0.005
predator_rate = 0.1

starvation_rate_baseline = 0.01
current_starvation_rate = starvation_rate_baseline * math.log(population, 10)

x_coord = []
y_coord = []

for i in range(0, 2 * day):
    for j in range(0, population):
        if random() <= birth_rate:
            population += int(triangular(1, 15, 10))
        if random() <= predator_rate:
            population -= 1
        if random() <= current_starvation_rate:
            population -= 1
        if random() <= death_rate:
            population -= 1



    x_coord.append(i * 12)
    y_coord.append(population)

plt.figure()
plt.plot(x_coord, y_coord)
plt.xlabel("Hours")
plt.ylabel("Population")
plt.title("Tribble Population Growth")
plt.show()
