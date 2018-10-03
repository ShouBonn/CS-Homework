# count = 0
# while count < 10:
#     print(count * 10)
#     count = count + 1

#
# count1 = 0
# while count1 >= -5:
#     print(count1)
#     count1 = round(count1 - 0.2, 2)


# b = 2
# a = 1
#
# for count in range(0, 5):
#     a = b * a + count
#     print(a)


# for num in range(1, 101):
#     if num % 3 and num % 8:
#         print(num)


height = 0
blank = " "
for height in range(4, 8):
    print(blank * height + "*")
for height in range(0, 4):
    height = -1 * height
    print(blank * height + "*")