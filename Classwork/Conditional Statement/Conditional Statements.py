##1
def driving_license(age):
    if age >= 18:
        return True
    else:
        return False

##2
def triangle_length(a, b, c):
    if a == b == c:
        print("Equilateral Triangle")
    elif (a == b) or (b == c) or (a == c):
        print("Isosceles Triangle")
    elif (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == b**2 + a**2):
        print("Right Triangle")
    elif (a**2 > b**2 + c**2) or (b**2 > a**2 + c**2) or (c**2 > b**2 + a**2):
        print("Obtuse Triangle")
    elif (a**2 < b**2 + c**2) or (b**2 < a**2 + c**2) or (c**2 < b**2 + a**2):
        print("Acute Triangle")
    elif (a > b + c) or (b > a + c) or (c > a + b):
        print("Not an Triangle at ALL")

##3
def trick(num):
    if num % 5 == 0 and num % 3 == 0:
        print("FIZZ BUZZ!")
    elif num % 5 == 0:
        print("BUZZ!")
    elif num % 3 == 0:
        print("FIZZ!")
    else:
        print("Huh?")

##4
from math import factorial
def combinations(n, r):
    c = factorial(n) / (factorial(n - r) * factorial(r))
    if c > 1000000:
        print("Give Up")
    elif 1000000 > c > 10000:
        print("Keep Trying")
    elif c < 10000:
        print("You're nearly there!")

##5
from random import random, randint
print(random())
print(randint(-10, 10))

def chocolate_box():
    ran = randint(0, 100)
    if ran == 87:
        print("How did I get so lucky?")
    elif ran <= 10:
        print("If laughter is the best medicine, your face must be curing the world.")
    elif 10 < ran <= 20:
        print("Brains aren't everything. In your case they're nothing.")
    elif 20 < ran <= 30:
        print("I can lose weight, but you’ll always be ugly.")
    elif 30 < ran <= 40:
        print("You're the reason the gene pool needs a lifeguard.")
    elif 40 < ran <= 50:
        print("Calling you an idiot would be an insult to all the stupid people.")
    elif 50 < ran <= 60:
        print("You are not as bad as people say, you are much, much worse.")
    elif 60 < ran <= 70:
        input("How old are you:")
        print("Wait I shouldn't ask, you can't count that high.")
    elif 70 < ran <= 80:
        print("Stupidity is not a crime so you are free to go.")
    elif 80 < ran <= 90:
        print("If I had a face like yours, I'd sue my parents.")
    elif 90 < ran <= 100:
        print("My friend thinks he is smart. He told me an onion is the only food that makes you cry, so I threw a coconut at his face.")

##6
def roll_dice(a, b, c):
    guess = 0
    ran = randint(1, 6)
    if a == ran:
        guess += 1
    if b == ran:
        guess += 1
    if c == ran:
        guess += 1
    print("number of guesses correct:", guess)