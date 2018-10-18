DISTRICTS = 92
parties = ['Tea Party', 'Coffee Party', 'Milk Party','House Party', 'Beach Party']


def init_election():
    return [[0 for i in range(len(parties))]
               for j in range(DISTRICTS)]


election = init_election()


def update_election(valgdata, valgdistrikt, stemmer):
    for i in range(len(parties)):
        valgdata[valgdistrikt - 1][i] += stemmer[i]

    return valgdata

election = update_election(election, 1, [12, 1, 1, 1, 1])
election = update_election(election, 2, [1, 1, 1, 1, 1])
election = update_election(election, 3, [235728734, 18488234, 234, 34563425, 23444])
election = update_election(election, 4, [235728734, 18488234, 234, 34563425, 23444])
election = update_election(election, 5, [235728734, 18488234, 234, 34563425, 23444])
election = update_election(election, 6, [23, 14, 234, 1, 1])
election = update_election(election, 8, [23, 14000000, 234, 1, 1])
election = update_election(election, 9, [235728734, 18488234, 234, 34563425, 23444])
election = update_election(election, 10, [1, 1, 234, 1, 1])
election = update_election(election, 12, [1, 234, 234, 1, 1])
election = update_election(election, 90, [230000, 1, 234, 3, 23444])
election = update_election(election, 89, [230000, 1, 234, 3, 23444])


def print_lead(election, parties):
    total = [0 for i in range(len(parties))]

    for i in range(len(parties)):
        for j in range(DISTRICTS):
            total[i] += election[j][i]

    max_index = total.index(max(total))

    print(parties[max_index], 'is leading the election with', total[max_index], 'votes.')


def district_count(election, parties):
    total = [0 for i in range(len(parties) + 2)]

    for i in range(DISTRICTS):
        if max(election[i]) == 0:
            total[6] += 1
        else:
            max_index = election[i].index(max(election[i]))

            for j in range(len(parties)):
                if max(election[i]) == election[i][j] and j != max_index:
                    total[5] += 1
                    break
            else:
                total[max_index] += 1
    return total


def delegate(x):
    if x > 1 or x == 0:
        return 'delegates'
    else:
        return 'delegate'


def print_results(election, parties):
    new_list = parties + ['Undecided (tied)', 'Undecided (no votes)']

    count = district_count(election, parties)

    for i in range(len(new_list)):
        print((new_list[i] + ':').ljust(30), end="")
        print(str(count[i]).rjust(5), end=" ")
        print(delegate(count[i]))


print_results(election, parties)