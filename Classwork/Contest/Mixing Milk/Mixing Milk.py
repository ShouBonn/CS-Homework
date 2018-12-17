with open('mixmilk.in', 'r') as f:
    lines = f.readlines()

capacity1, milk1 = lines[0].strip().split()
capacity1 = int(capacity1)
milk1 = int(milk1)

capacity2, milk2 = lines[1].strip().split()
capacity2 = int(capacity2)
milk2 = int(milk2)

capacity3, milk3 = lines[2].strip().split()
capacity3 = int(capacity3)
milk3 = int(milk3)


def mixing(milk1, milk2, milk3, capacity1, capacity2, capacity3):
    count = 0

    while count < 99:
        if (milk1 + milk2) <= capacity2:
            milk2 += milk1
            milk1 = 0
        elif (milk1 + milk2) > capacity2:
            milk1 = (milk2 + milk1) - capacity2
            milk2 = capacity2
        count += 1
        print(count, ':', str(milk1+milk2+milk3), milk1, milk2, milk3)

        if (milk2 + milk3) <= capacity3:
            milk3 += milk2
            milk2 = 0
        elif (milk2 + milk3) > capacity3:
            milk2 = (milk2 + milk3) - capacity3
            milk3 = capacity3
        count += 1
        print(count, ':', str(milk1+milk2+milk3), milk1, milk2, milk3)

        if (milk1 + milk3) <= capacity1:
            milk1 += milk3
            milk3 = 0
        elif (milk1 + milk3) > capacity1:
            milk3 = (milk1 + milk3) - capacity1
            milk1 = capacity1
        count += 1
        print(count, ':', str(milk1+milk2+milk3), milk1, milk2, milk3)

    if (milk2 + milk1) <= capacity2:
        milk2 += milk1
        milk1 = 0
    elif (milk2 + milk1) > capacity2:
        milk1 = (milk2 + milk1) - capacity2
        milk2 = capacity2
    print(milk1, milk2, milk3)

    return milk1, milk2, milk3

m1, m2, m3 = mixing(milk1, milk2, milk3, capacity1, capacity2, capacity3)

with open('mixmilk.out', 'w') as f:
    f.write(str(m1) + '\n')
    f.write(str(m2) + '\n')
    f.write(str(m3) + '\n')