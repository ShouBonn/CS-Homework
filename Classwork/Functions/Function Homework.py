import math
#1
def mixed_number(num1, num2):
    whole = num1//num2
    remainder = num1%num2
    print(whole, str(remainder) + "/" + str(num2))

#2
def vowel_count(string, vowel):
    return string.count(vowel)

def vowel_total(string):
    return vowel_count(string, "a") + vowel_count(string, "e") + vowel_count(string, "i") + vowel_count(string, "o") + vowel_count(string, "u")

#3
def individual_vowel_count(string):
    print("a", "e", "i", "o", "u")
    print(vowel_count(string, "a"), vowel_count(string, "e"), vowel_count(string, "i"), vowel_count(string, "o"), vowel_count(string, "u"))
    return vowel_count(string, "a"), vowel_count(string, "e"), vowel_count(string, "i"), vowel_count(string, "o"), vowel_count(string, "u")

#4
def return_value(string):
    a = vowel_count(string, "a")
    e = vowel_count(string, "e")
    i = vowel_count(string, "i")
    o = vowel_count(string, "o")
    u = vowel_count(string, "u")
    return a, e, i, o, u

#5
def volume_sphere(r):
    return 4/3 * math.pi * r**3

def surface_area_sphere(r):
    return 4 * math.pi * r**2

#6
def display(r):
    print("volume of sphere with radius", str(r) + "cm:", str(volume_sphere(r)), "cm^3")
    print("surface area of sphere with radius", str(r) + "cm:", str(surface_area_sphere(r)), "cm^2")

#7
def information(name = "Tom Cruise", age = 87, weight = 99):
    print (name, age, weight)

information()
information("William")
information("William", 16)
information("William", 16, 56)
information(age = 16)
information(weight = 56)
information(name = "William", weight = 80)
information(age = 16, weight = 56)


#8
def color_hex(num1, num2, num3):
    return (hex(num1), hex(num2), hex(num3))

def color_bin(num1, num2, num3):
    return (bin(num1), bin(num2), bin(num3))
