lists = [[ 0 for x in range(3)] for y in range(3)]

for list in lists:
    print(list)


tall = 2
for x in range(3):
    for y in range(3):
        lists[x][y] = tall
        tall += 2

for list in lists:
    print(list)

