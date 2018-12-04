# print(str(52) + "\n" + bin(52) + "\n" + hex(52))
#
# a = "*"
# print( a + "\n" + 2*a + "\n" + 3*a + "\n" + 4*a + "\n" + 5*a)
#
# print(pow(2,11))
#
# def dododo(x, y):
#     print(x + y)
#
# def hibye(g, h, j):
#     str(g)
#     str(h)
#     int(j)
#     print((g + h) * j)
#
# print(hibye("Hi", "Bye", 8))
#
# a = 7.0
#
# if a == int(a):
#     print("integer")
# else:
#     print("non-integer")
#
# a = 10
# b = 2
# print("Yes") if a < b else print("Winner") if a**b <= 100 else print("No")
#
#
# a = 10
#
# if a**0.5 < 5 or a**0.5 > 10:
#     print("Yup")
# elif a**0.5 == 10:
#     print("=10")
# else:
#     print("None")
#
# str1 = 'sedrtyuidfg1345jk'
#
# if str1.isalpha() and len(str1) < 30:
#     print("Valid")
# else:
#     print("Invalid Name")
#
#
# def perfect_number(num):
#     total = 0
#     for i in range(1, num):
#         if num % i == 0:
#             total += i
#     return total == num
#
# print(perfect_number(6))
#
# a = 0
# num=6
# while a <= 10:
#     if perfect_number(num) == True:
#         print(num)
#         a += 1
#     num += 1

# warmup = ['a', 'z', 'd', 'g']
#
# var1 = warmup[0]
# warmup[0] = warmup[3]
# warmup[3] = var1
#
# print(warmup)
#
#
# warmup1 = ['a', 'z', 'd', 'g']
# print(warmup1[1:3] + warmup1 + warmup1[1:3])
#
#
# warmup2 = ['a', 'z', 'd', 'g']
# for i in range(0, len(warmup2)):
#     for j in range(0, 5):
#         print(warmup2[i], end = ' ')
#     print()
#
# import random
# new = []
#
# for i in range(0, 100):
#     g = random.randint(1, 100)
#     if g % 2 == 1 and g % 7 != 0:
#         new.append(g)
#
# print(new[0:])
#
# def even_numbers(lst):
#     new_lst = []
#     for item in lst:
#         if item % 2 == 0:
#             new_lst.append(item)
#     return new_lst
#
# print(even_numbers([2, 3, 5, 6, 7, 8, 4, 3, 3]))
#
# def smallest_number(lst):
#     return sorted(lst)[:2]
#
# def organize(lst):
#     letters = []
#     integers = []
#     for item in lst:
#         if type(item) == str:
#             letters.append(item)
#         else:
#             integers.append(item)
#     return letters, integers

# import random
#
# integer = {}
# for i in range(10):
#     integer[i] = 0
#
# for i in range(10000):
#     integer[random.randint(0, 9)] += 1
#
# for i in range(10):
#     print('Num ', i, ": ", integer[i])


a = [1, -3, 5, 7, 15, -4, 0, -6, -10, -11, 12]

def sort_odd_and_even(lst):
    for j in range(len(lst)):
        for i in range(len(lst)):
            num = lst[i]
            if abs(lst[i]) % 2 == 0:
                lst.pop(i)
                lst.append(num)
    return lst


def sort_positive_and_negative(lst):
    for j in range(len(lst)):
        for i in range(len(lst)):
            num = lst[i]
            if lst[i] < 0:
                lst.pop(i)
                lst.append(num)
    return lst

print(sort_positive_and_negative(a))