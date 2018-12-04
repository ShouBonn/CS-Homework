##1
def sixsixsix(lst):
    if lst[0] == 6 or lst [-1] == 6:
        print(True)
    return False

##2
def reverse(lst):
    first_term = lst[0]
    lst[0] = lst[-1]
    lst[-1] = first_term
    return lst

##3
def create(lst):
    new_lst = []
    new_lst += [lst[0]]
    new_lst += [lst[-1]]
    return new_lst

##4
def check(lst):
    for item in lst:
        if item == 2 or item == 3:
            return True
    return False

##5
def even_numbers(lst):
    count = 0
    for item in lst:
        if item % 2 == 0:
            count += 1
    return count

##6
def sum_of_list(lst):
    flaw = 0
    for i in range(len(lst)):
        if len(lst) - 1 == i and lst[i] == 13:
            flaw += 13
        elif lst[i] == 13:
            flaw += 13
            flaw += lst[i+1]
    return sum(lst) - flaw

##7
def mean(lst):
    lst=lst[:-1]
    lst.pop(0)
    return sum(lst) / len(lst)

##8
def palindrome(lst):
    lst_a = lst[:int(len(lst) / 2)]
    lst_b = lst[-len(lst_a):]
    if lst_b[::-1] == lst_a:
        print("Palindrome!!!")
    else:
        print("Try Again!!!")

##9
def easy_fun(lst):
    no_dup = set(lst)
    print(no_dup)

def duplicate(lst):
    upper = list(map(str.upper, lst))
    show = []
    for item in upper:
        if item not in show:
            show.append(item)
    print(show)

##10
import random

def ran_3D_coor(num):
    lst = []

    for i in range(0, num):
        ran1 = random.randint(-100, 100)
        ran2 = random.randint(-100, 100)
        ran3 = random.randint(-100, 100)
        lst.append((ran1, ran2, ran3))
    return lst

def _3D_distance(num):
    lst = ran_3D_coor(num)
    coord1 = None
    coord2 = None
    min_dist = 999999999999

    for i in range(0, len(lst)):
        for j in range(i + 1, len(lst)):
            x,y,z = lst[i]
            x1,y1,z1=lst[j]

            d = ((x - x1)**2 + (y - y1)**2 + (z - z1)**2)**0.5
            if d < min_dist:
                min_dist = d
                coord1 = lst[i]
                coord2 = lst[j]

    return coord1, coord2, min_dist

##11
import random

lst = []
num = 0

for i in range(100):
    lst.append(random.randint(0, 1000))

lst = sorted(lst)

for i in range(len(lst) - 1):
    if (lst[i] + 20 < lst[i + 1]):
        num += 1