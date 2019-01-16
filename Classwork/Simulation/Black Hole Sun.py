from random import randint

Dice = ["Up", "Down", "Left", "Right"]

coord = []

for i in range(4):
    coord.append([])
    for j in range(4):
        if randint(0, 100) <= 50:
            coord[i].append([[j, i], "Black Hole"])
        else:
            coord[i].append([[j, i], "Block"])

coord[0][0][1] = "Block"
coord[3][3][1] = "$"

print(coord[0])
print(coord[1])
print(coord[2])
print(coord[3])

times_of_rolling_dice = 10
try_again = 0
money_earned = 0
current_position = [0, 0]

for i in range(times_of_rolling_dice):
    roll = randint(0, 3)

    for j in range(4):
        for k in range(4):
            if current_position == coord[j][k][0]:
                if coord[j][k][1] == "Black Hole":
                    try_again += 1
                    current_position = [0, 0]
                    print("Black Hole!!! Reset to Origin")
                    response = input("Continue?")
                    if response == "N" or "No" or "n" or "no":
                        times_of_rolling_dice = 0
                # how do i stop or break the loop?

                else:
                    money_earned += 1
            elif current_position == [3, 3]:
                money_earned += 25
                print("YOU WON!!! WELL DONE!!!")

    if Dice[roll] == "Up":
        if 0 < current_position[1] < 4:
            current_position[1] -= 1
            print("Up")
        else:
            print("NO MOVE")
    elif Dice[roll] == "Down":
        if -1 < current_position[1] < 3:
            current_position[1] += 1
            print("Down")
        else:
            print("NO MOVE")
    elif Dice[roll] == "Left":
        if 0 < current_position[0] < 4:
            current_position[0] -= 1
            print("Left")
        else:
            print("NO MOVE")
    elif Dice[roll] == "Right":
        if -1 < current_position[0] < 3:
            current_position[0] += 1
            print("Right")
        else:
            print("NO MOVE")


    print(current_position)

print(try_again)
print(money_earned)
