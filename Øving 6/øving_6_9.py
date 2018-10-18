import numpy as np

def all_unique(lst):
    return len(set(lst)) == len(lst)

def remove_duplicates(lst):
    return list(set(lst))


def in_a_but_not_b(a, b):
    return list(set(a) - set(b))


def are_orthogonal(a, b):
    return np.dot(np.array(a), np.array(b)) == 0


arr = np.arange(1, 16)

arr = arr.reshape((3, 5))

arr = np.transpose(arr)

print(arr)