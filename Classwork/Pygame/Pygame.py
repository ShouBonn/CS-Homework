##1
# import pygame
# screen = pygame.display.set_mode((1000, 1000))
#
# running = True
#
# r = 0
# g = 0
# b = 0
#
# rinc = 0
# ginc = 3
# binc = 0
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     pygame.draw.circle(screen, (r, g, b), (500, 500), 200)
#     pygame.display.update()
#
#     r = r + rinc
#     g = g + ginc
#     b = b + binc
#
#     if g >= 255 or g <= 0:
#         rinc = rinc * -1
#         ginc = ginc * -1
#         binc = binc * -1
#
# pygame.quit()

##2
import pygame
screen = pygame.display.set_mode((500, 100))
clock = pygame.time.Clock()

running = True

rad = [50,50,50,50,50]
radinde = [-1,-2,-5,-10,-25]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(0, 5):
        pygame.draw.circle(screen, (200, 100, 200), (50 + 100 * i, 50), rad[i])

    pygame.display.update()

    for i in range(0, 5):
        if rad[i] <= 50 and rad[i] > 0:
            rad[i] += radinde[i]

    clock.tick(60)

pygame.quit()

#3
# import pygame
# import random
# screen = pygame.display.set_mode((600, 600))
# clock = pygame.time.Clock()
#
# running = True
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     for i in range(0, 30):
#         ran = random.randint(0, 255)
#         ran1 = random.randint(0, 255)
#         ran2 = random.randint(0, 255)
#         pygame.draw.circle(screen, (ran, ran1, ran2), (300, 300), 300 - 10 * i)
#
#     pygame.display.update()
#     clock.tick(60)
#
# pygame.quit()
