from time import time
from random import randint

def rand_list(upper, lower, size):
    rnd_list = []
    for i in range(size):
        rnd_list.append(randint(lower, upper))
    return rnd_list



def bubble_sort(list):
    list_sorted = False
    sort_range = len(list) - 1
    new_sort_range = 0
    while not list_sorted:
        list_sorted = True
        for i in range(sort_range):
            if list[i] > list[i + 1]:
                list_sorted = False
                list[i], list[i + 1] = list[i + 1], list[i]
                new_sort_range = i
        sort_range = new_sort_range

    return list


def selection_sort(list):
    new_list = []
    while len(list) > 0:
        high = 0
        for number in list:
            if number > high:
                high = number

        new_list.append(high)
        list.remove(high)

    return new_list


random_list = rand_list(1000, 0, 100)

time_0 = time()
print(bubble_sort(random_list))
time_1 = time()
print('Bubble sort run time:', time_1-time_0)

time_0 = time()
print(selection_sort(random_list))
time_1 = time()
print('Selection sort run time:', time_1-time_0)
