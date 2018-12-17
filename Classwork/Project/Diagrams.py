import matplotlib.pyplot as plt
import math

def f(data):
    return [math.cos(val) for val in data]

def g(data):
    return [math.sin(val) for val in data]

t = [val/math.pi for val in range(0, 100)]
plt.plot(t, f(t), t, g(t))
plt.show()