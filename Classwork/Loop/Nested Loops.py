# ##1
# for length in range(1, 6):
#     print(10 * "*")
#
##2
# for x in range(0,5):
#     print(" " * (5-x),end="*")
#     print("*" * 2 * x)
#     print()

##3
def box(l, w):
    if (l % 2 == 1) and (w % 2 == 1):
        print(w * '* ', end= '')
        print()
        for i in range(int((l-2)/2)):
            print('*', (i) * ' ' + "*" + (5 - 2 * (i+1)) * ' ' + '*', '*')

        print(int(l/2) * ' ' + '*')

        for i in range(int((l-2)/2)):
            a = 1 - i
            print('*', a * ' ' + '*' + (5 - 2 * (a + 1)) * ' ' + '*', '*')

        print(w * '* ', end='')


box(5, 5)
print()

for i in range(2):
    print(i * ' ' + "*" , (5 - 2 * (i+1)) * ' ' , '*')

print(2 * ' ' + '*')

for i in range(2):
    a = 1 - i
    print(a * ' ' + '*' + (5 - 2 * (a+1)) * ' ' + '*')




##4
# import pygame
# screen = pygame.display.set_mode((500, 500))
#
# running = True
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.fill((0, 0, 0))
#
#     for j in range(5):
#         for i in range(5):
#             if (j+i) % 2 == 1:
#                 pygame.draw.rect(screen, (255, 255, 255), ((i * 100, j * 100), (100, 100)))
#
#
#     pygame.display.update()
# pygame.quit()
#

# git add*
# git commit -m "Logo"
# git push origin master

