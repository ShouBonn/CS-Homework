import module1

print(module1.var1)

module1.say_hello()



from module1 import say_hello

say_hello()



def say_hello(Name = "Mr.Bach"):
    print(Name + ",", "you smell bad!!")

say_hello()



import math

print(math.log(5,10))
print(math.radians(300))
print(math.exp(4))
print(math.factorial(6))
print(math.atan(3))



from math import sqrt

print(sqrt(25))

def sqrt(x):
    return x**0.5

print(sqrt(25))
