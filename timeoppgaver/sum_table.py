def sum_table(table):
    sum = 0
    for i in range(len(table)):
        for j in range(len(table[i])):
            sum += table[i][j]
    return sum


my_list = [[1 for i in range(10)] for i in range(5)]



print(sum_table(my_list))