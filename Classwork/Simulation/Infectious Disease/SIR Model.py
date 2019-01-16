import matplotlib.pyplot as plt

susceptible = 0.95
infected = 0.05
recovered = 0
susceptible_infected = 1
infected_recovered = 0.1
steps = 100

x_coord_steps = []
y_coord_susceptible = []
y_coord_infected = []
y_coord_recovered = []

for i in range(0, steps):
    x_coord_steps.append(i)
    y_coord_susceptible.append(susceptible)
    y_coord_infected.append(infected)
    y_coord_recovered.append(recovered)

    new_infected = infected_recovered * susceptible * infected
    new_recovered = infected_recovered * infected

    susceptible -= new_infected
    infected += (new_infected - new_recovered)
    recovered += new_recovered


plt.figure()
plt.plot(x_coord_steps, y_coord_susceptible, label = 'Susceptible')
plt.plot(x_coord_steps, y_coord_infected, label = 'Infected')
plt.plot(x_coord_steps, y_coord_recovered, label = 'Recovered')
plt.legend(loc = 'upper right')
plt.xlabel("Days")
plt.ylabel("Fraction of Population")
plt.title("Infection Diseases")
plt.show()
