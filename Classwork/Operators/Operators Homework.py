##1
#1
print(9 % 7)
#2
print(8 * 4 - 4)
#3
print(bool(4))
#4
print((10 + 4) * abs(1))
#5
print(pow(2 , (4 % 4)))
#6
print(20 - int(14.5))
#7
print(bool(10 - 5 * int(2.2)))
#8
print(divmod(19 , 4))
#9
print(str(5 * 10 - (13 + 5)))
#10
print(float(4 - 15 % 4 + int(True)))

##2
"Integer"
"String"
"Float"

##3
"Boolean"

##4
"var1 += 1"
"quicker, easier to understand"

##5
#1
print(bool(3 < 4 and 2 > 1))
#2
print(bool(len("Hi") < 3))
#3
print(bool(6 < 8 or 10 > 12))
#4
print(bool(not 7 > 10))
#5
print(bool(5 < 6 and 7 > 8))
#6
print(bool(not(5 > 6 and 7 < 8)))
#7
print(bool(('A' != 'B') and (10 / 5) == 2))
#8
print(bool(('A' != 'B') and (5 / 10) == 2))

##6
#1
a = 10
b = 100 - 1
print(a , b)
#2
var1 = 100
var2 = 50
var1 += 10
print(var1)
#3
a = "Hi"
b = "Bye"
a += a + b
a *= 2
print(a)
#4
my_name = "Mr. Bach"
your_name = "Mr. Student"
print(my_name + " or " + your_name + "?")
#5
this_val = False
that_val = True
some_val = 0
this_val += 1
print(this_val)
this_val and that_val == False
print(some_val + 0)

##7
def quadratic(a, b, c):
    root1 = ((-b + (b**2 - 4*a*c)**0.5) / 2*a)
    root2 = ((-b - (b**2 - 4*a*c)**0.5) / 2*a)
    print(root1, root2)

##8
def logic_circuit(a, b, c):
    x = a and b
    y = not(a and c)
    return bool(x or y)

for i in range(0, 2):
    for j in range(0, 2):
        for k in range(0, 2):
            result = logic_circuit(i, j, k)
            print(i, j, k, result)