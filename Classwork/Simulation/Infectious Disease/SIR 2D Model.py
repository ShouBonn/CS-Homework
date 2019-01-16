from gridworld import GridWorld
from random import randint

simulation = GridWorld(100, 80, 10)

color = simulation.get_cell(10, 10)

colors = [(200, 0, 0), (0, 200, 0), (0, 0, 200)]
for i in range(1000):
    simulation.set_cell(randint(0, 100), randint(0, 80), colors[randint(0, 2)])

time = 100


def three_blocks_first_last(line):
    rate1 = 0
    for item in s[line]:
        if type(item) == tuple:
            if item[0] == 200:
                rate1 += 2
    return rate1


def three_blocks_zero_six(line):
    rate2 = 0
    if type(s[line][0]) == tuple:
        if s[line][0][0] == 200:
            rate2 += 2
    if type(s[line][6]) == tuple:
        if s[line][6][0] == 200:
            rate2 += 2
    return rate2


def two_blocks_first_last(line):
    rate3 = 0
    for i in range(5):
        if type(s[line][i + 1]) == tuple:
            if s[line][i + 1][0] == 200:
                rate3 += 5
    return rate3


def two_blocks_one_five(line):
    rate4 = 0
    if type(s[line][1]) == tuple:
        if s[line][1][0] == 200:
            rate4 += 5
    if type(s[line][5]) == tuple:
        if s[line][5][0] == 200:
            rate4 += 5
    return rate4


def adjacent_first_last(line):
    rate5 = 0
    for i in range(3):
        if type(s[line][i + 2]) == tuple:
            if s[line][i + 2][0] == 200:
                rate5 += 25
    return rate5


def adjacent_two_four(line):
    rate6 = 0
    if type(s[line][2]) == tuple:
        if s[line][2][0] == 200:
            rate6 += 25
    if type(s[line][4]) == tuple:
        if s[line][4][0] == 200:
            rate6 += 25
    return rate6

info = {}
for cell in simulation.cells:
    info[cell[0], cell[1]] = [simulation.cells[cell], 0]

for i in range(time):
    for cell in simulation.cells:
        rate = 0
        s = simulation.get_surroundings(cell[0], cell[1], 3)
        rate = rate + three_blocks_first_last(0) + three_blocks_first_last(6) + three_blocks_zero_six(1) + three_blocks_zero_six(2) + three_blocks_zero_six(3) + three_blocks_zero_six(4) + three_blocks_zero_six(5) + two_blocks_first_last(1) + two_blocks_first_last(5) + two_blocks_one_five(2) + two_blocks_one_five(3) + two_blocks_one_five(4) + adjacent_first_last(2) + adjacent_first_last(4) + adjacent_two_four(3)
        if rate > 97:
            rate = 97
        if randint(0, 100) <= rate:
            simulation.cells[cell] = (200, 0, 0)

        if info[cell[0], cell[1]][0][0] == 200:
            info[cell[0], cell[1]][1] += 1
        if info[cell[0], cell[1]][1] > 3:
            if randint(0, 1000) <= 5:
                info[cell[0], cell[1]][0] = (0, 255, 255)
                simulation.set_cell(cell[0], cell[1], (0, 255, 255))
            else:
                info[cell[0], cell[1]][0] = (0, 0, 200)
                simulation.set_cell(cell[0], cell[1], (0, 0, 200))


done = False
while not done:
    done = simulation.process_events()
    simulation.update()

simulation.end()