##1
#a
34
#b
16
#c
27
#d
53

##2
a = 10
b = 20
c = 30


def foo1(a):
    a = b + c
    print(a)

##3
def add(num1, num2):
    return num1 + num2

def triple(num):
    return add(num, add(num, num))

def quadruple(nun):
    return add(nun, add(nun, add(nun, nun)))

