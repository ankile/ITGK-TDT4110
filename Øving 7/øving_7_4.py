from random import randint
import øving_7_8
from statistics import mode

# a)
random_numbers = []
for i in range(100):
    random_numbers.append(randint(1, 10))

print('random_numbers:', random_numbers, '\n')

# b)
print('Antallet 2ere i listen:', random_numbers.count(2), '\n')

# c)

print('Sum:', sum(random_numbers), '\n')

# d)
random_numbers = øving_7_8.bubble_sort(random_numbers)

print(random_numbers, '\n')

# e)
def typetall(liste):
    try:
        return mode(liste)
    except:
        return 'det var ingen unike typetall'


print('Typetall:', typetall(random_numbers), '\n')

# f)
print(øving_7_8.selection_sort(random_numbers))