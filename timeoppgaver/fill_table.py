def fill_table(table):
    tall = 2
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = tall
            tall += 2
    # return table


my_list = [[0 for i in range(2)] for i in range(5)]

fill_table(my_list)

for row in my_list:
    print(row)