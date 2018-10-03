print(str(52) + "\n" + bin(52) + "\n" + hex(52))

a = "*"
print( a + "\n" + 2*a + "\n" + 3*a + "\n" + 4*a + "\n" + 5*a)

print(pow(2,11))

def dododo(x, y):
    print(x + y)

def hibye(g, h, j):
    str(g)
    str(h)
    int(j)
    print((g + h) * j)

print(hibye("Hi", "Bye", 8))

a = 7.0

if a == int(a):
    print("integer")
else:
    print("non-integer")

a = 10
b = 2
print("Yes") if a < b else print("Winner") if a**b <= 100 else print("No")


a = 10

if a**0.5 < 5 or a**0.5 > 10:
    print("Yup")
elif a**0.5 == 10:
    print("=10")
else:
    print("None")

str1 = 'sedrtyuidfg1345jk'

if str1.isalpha() and len(str1) < 30:
    print("Valid")
else:
    print("Invalid Name")

