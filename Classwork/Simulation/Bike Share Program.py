import random

Station1 = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
Station2 = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]

Time = 3
RateS1 = 3
RateS2 = 4

for i in range(Time):
    count1 = []
    count2 = []

    for i in range(len(Station1)):
        if Station1[i] == 1:
            count1.append(i)

    for i in range(len(Station2)):
        if Station1[i] == 1:
            count1.append(i)

    if len(count1) >= 3:
        for i in range(3):
            rent = random.randint(0, len(count1))
            renting_bike = count1[rent]
            Station1[count1[rent]] = 0
    else:
        for i in range(len(count1)):
            rent = random.randint(0, len(count1))
            renting_bike = count1[rent]
            Station1[count1[rent]] = 0

    if len(count1) >= 4:
        for i in range(4):
            rent = random.randint(0, len(count1))
            renting_bike = count1[rent]
            Station1[count1[rent]] = 0
    else:
        for i in range(len(count1)):
            rent = random.randint(0, len(count1))
            renting_bike = count1[rent]
            Station1[count1[rent]] = 0

    space1 = []
    space2 = []

    for i in range(len(Station1)):
        if Station1[i] == 0:
            space1.append(i)

    for i in range(len(Station2)):
        if Station1[i] == 0:
            space2.append(i)

    for i in range(7):
        probability = random.randint(0, 100)/100
        if probability >= 0.5:
            if len(space1) > 0:
                space_id = space1[random.randint(len(space1))]
                Station1[space_id] = 1
            else:
                space_id = space2[random.randint(len(space2))]
                Station2[space_id] = 1
        else:
            if len(space2) > 0:
                space_id = space2[random.randint(len(space2))]
                Station2[space_id] = 1
            else:
                space_id = space1[random.randint(len(space1))]
                Station1[space_id] = 1
    print(Station1)
    print(Station2)