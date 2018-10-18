def file_to_list(filename):
    f = open(filename)
    list = f.readlines()
    f.close()

    for i in range(len(list)):
        list[i] = list[i].split(',')
        list[i][2] = float(list[i][2])

    return list


def list_stores(data_list):
    list_of_stores = []
    for row in data_list:
        if row[0] not in list_of_stores:
            list_of_stores.append(row[0])

    return list_of_stores


def sum_prices_stores(data_list, store_list):
    liste = []
    for butikk in store_list:
        subtotal = 0
        for row in data_list:
            if butikk == row[0]:
                subtotal += row[2]
        liste.append(subtotal)
    return liste


def rank_stores(store_list, sum_stores):
    list = []
    for i in range(len(sum_stores)):
        elem = min(sum_stores)
        index = sum_stores.index(elem)
        sum_stores.pop()
        list.append(store_list[index])


    return list



data_list = file_to_list('pricewar.txt')

store_list = list_stores(data_list)

sum_stores = sum_prices_stores(data_list, store_list)
print(sum_stores)


sorted_list = rank_stores(store_list, sum_stores)

print(data_list)

print(store_list)

print(sorted_list)

def store_analysis(filename):
    data_list = file_to_list(filename)

    store_list = list_stores(data_list)

    sum_stores = sum_prices_stores(data_list, store_list)

    print("The total price for shopping per store is:")

    for i in range(len(store_list)):
        print(store_list[i], ':', sum_stores[i], 'kr')

    print()

    sorted_list = rank_stores(store_list, sum_stores)


    print('The ranking of stores according to prices is:')
    for i in range(len(sorted_list)):
        print(i + 1, sorted_list[i])


store_analysis('pricewar.txt')















