
def add(p1, p2, p3):
    return p1+p2+p3
def multiply(p1, p2):
    return p1*p2
def power(p1, p2):
    return pow(multiply(p1, p2), p2)
print(power(78, 9))
print(multiply(56, 67))
print(add(1, 2, 3))

def powerpower(p1, p2, p3, p4, p5):
    return pow(p1, p2) ** p3 ** p4 ** p5

print(powerpower(34, 5, 6, 7, 8))
