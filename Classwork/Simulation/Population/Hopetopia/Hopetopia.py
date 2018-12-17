import matplotlib.pyplot as plt
from random import random, randint

male = 84
female = 91
population = male + female

witch = 0
successful_potion_rate = 0.01

Disasters = ["Tsunami", "Typhoon", "Earthquake", "Barbarian Invasion"]

year = 100

x_coord = []
male_coord = []
female_coord = []
population_coord = []

for i in range(year):
    for j in range(int(female * 0.6)):
        if random() <= 0.3:
            if random() <= 0.5:
                male += 1
            elif random() <= 0.0001:
                witch += 1
            else:
                female += 1
    population = male + female

    dead_people = int(0.05 * population)
    distribution = randint(0, dead_people)
    male -= distribution
    female -= (dead_people - distribution)

    population = male + female

    if population > 1000:
        print(87654)
        if witch > 0:
            if random() <= successful_potion_rate:
                print("Black Death!!!")
                dead_men = int(0.3 * male)
                dead_women = int(0.3 * female)
                male -= dead_men
                female -= dead_women
                casualties = dead_men + dead_women
                print("Casualties:", casualties)
        else:
            lottery = randint(0, 3)
            print(Disasters[lottery], "!!!")
            dead_men = int(0.7 * male)
            dead_women = int(0.7 * female)
            male -= dead_men
            female -= dead_women
            casualties = dead_men + dead_women
            print("Casualties:", casualties)

    population = male + female

    x_coord.append(i)
    male_coord.append(male)
    female_coord.append(female)
    population_coord.append(population)

    print(population)

plt.figure()
plt.plot(x_coord, male_coord)
plt.plot(x_coord, female_coord)
plt.plot(x_coord, population_coord)
plt.xlabel("Years")
plt.ylabel("Population")
plt.title("Hopetopia Population Growth")
plt.show()