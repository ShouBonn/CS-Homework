##1
count = 8
for whole_numbers in range (12):
    print(count - whole_numbers)

whole_number = 8
while whole_number >= -3:
    print(whole_number)
    whole_number -= 1

##2
def is_odd(num):
    if num%2 == 0:
        return False
    else:
        return True

for num in range(1, 10):
    if is_odd(num) == True:
        print("odd")
    else:
        print("even")

##3
from random import randint

def dice_roll(times):
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    for value in range(times):
        times * randint(1, 6)
        if 1 == randint(1, 6):
            one += 1
        elif 2 == randint(1, 6):
            two += 1
        elif 3 == randint(1, 6):
            three += 1
        elif 4 == randint(1, 6):
            four += 1
        elif 5 == randint(1, 6):
            five += 1
        elif 6 == randint(1, 6):
            six  += 1
    print("One:", one, "\n" + "Two:", two, "\n" + "Three:", three, "\n" + "Four:", four, "\n" + "Five:", five, "\n" + "Six:", six, "\n")

##4
def digit_magic(num):
    num = str(num)
    odd = 0
    even = 0

    for digit in num:
        digit = int(digit)
        if digit % 2 == 1:
            odd += 1
        elif digit % 2 == 0:
            even += 1
    print(odd, even)
