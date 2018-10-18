from random import randint

# a)
def rand_list(size, lower_bound, upper_bound):
    list =[]
    for i in range(size):
        list.append(randint(lower_bound, upper_bound))

    return list


# b)
def compare_lists(list1, list2):
    list1 = set(list1)
    list2 = set(list2)

    new_list = []
    for i in list1:
            if list1[i] in list2:
                new_list.append(i)
    return list(new_list)


# c)
def multi_comp_list(lists):
    new_list = list(set(lists[0]))

    for i in lists[0]:
        for j in range(1, len(lists)):
            if i not in lists[j] and i in new_list:
                new_list.remove(i)

    return new_list


a = [1, 2, 3, 4, 5, 4]
b = [2, 3, 4, 4, 5]
c = [2, 4, 5]
e = [1, 2, 3, 4, 5, 6]
f = [1, 2, 3, 4]
d = [a, b, c, e, f]


# d)
def longest_even(list):
    init_index = 0
    init_row = 0
    for i in range(len(list)):
        new_index = 0
        new_row = 0
        if list[i] % 2 == 0:
            new_index = i
            for j in range(i+1, len(list)):
                if list[j] % 2 == 0:
                    new_row += 1
                else:
                    break

        if new_row > init_row:
            init_index = new_index
            init_row = new_row

    return init_index, init_row


longest_even([2, 4, 2, 2, 2, 2, 5, 6, 8, 2, 4, 3])



def main():
    print(rand_list(10, 2, 7))
    a = [1, 2, 3]
    b = [4, 3, 1]
    print(compare_lists(a, b))
    c = [7, 2, 1]
    d = [a, b, c]
    print(multi_comp_list(d))
    list = [4, 3, 3, 6, 2, 6, 8, 3, 4, 3, 3]
    print(longest_even(list))


main()