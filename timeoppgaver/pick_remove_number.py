import random

def pick_remove_number(list):
    index = random.randint(0, len(list) - 1)
    return list.pop(index)


def Pick_remove_number(list):
    return random.choice(list)


A = [2, 3, 4, 5, 6, 7, 8, 9]


print(pick_remove_number(A))

print(A)

print(Pick_remove_number(A))

print(A)