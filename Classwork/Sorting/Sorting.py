def bubble_sort(lst):
    tem = 0
    for i in range(len(lst)):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                tem = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = tem
    return lst

#
# def selection_sort(lst):
#     current_position = 0
#     smallest = 0
#     swap = 0
#     for i in range(len(lst) - 1):
#         if lst[current_position] > lst[i]:
#             smallest = lst[i]
#             smallest_index = i
#             lst[current_position] = swap
#             lst[current_position] = lst[i]
#             lst[i] = swap
#         current_position += 1
#
#     return lst
#
# print(selection_sort([3, 6, 4, 7, 5, 9, 1]))


# def insertion_sort(lst):
#     swap = 0
#     for i in range(len(lst)):
#         if lst[i] > lst[i + 1]:
#             swap = lst[i + 1]
#             lst[i] =



# lst = [3, 4, 5, 6, 7, 8]
# print(lst[])


# def insertion_sort(lst):
# #     for i in range(1, len(lst)):
# #         print(lst)
# #         current_value = lst[i]
# #         j = i - 1
# #         while j >= 0 and current_value < lst[j]:
# #             lst[j + 1] = lst[j]
# #             j -= 1
# #         lst[j + 1] = current_value
# #     return lst
# #
# #
# # lst = [8, 7, 6, 5, 4, 3, 2, 1]
# # insertion_sort(lst)

import random

lst = sorted([random.randint(1, 100000000)] for i in range(1000000))
print("sorted")

index = []
for i in range(len(lst)):

    index.append((i,lst[i]))


def binary_search(lst, search_for):
    while len(lst) > 1:
        location = int(len(lst) / 2)
        if lst[location][1] == search_for:
            return True, lst[location][0]
        elif lst[location][1] > search_for:
            lst = lst[:location]
        else:
            lst = lst[location:]
    return False


print(binary_search(index, 4))
