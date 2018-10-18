hs = {}

hs[1] = ['Albus', 100]
hs[2] = ['Frank', 90]
hs[3] = ['Fleur', 80]
hs[4] = ['Sirius', 70]
hs[5] = ['vernon', 60]
hs[6] = ['Ron', 50]
hs[7] = ['Harry', 40]
hs[8] = ['Minerva', 30]
hs[9] = ['Hermine', 20]
hs[10] = ['Severus', 10]


def check_highscore(points, scores):
    for place in scores:
        if points > scores[place][1]:
            return place
    return -1

print(check_highscore(48, hs))

def add_highscore(points, name, scores):
    place = check_highscore(points, scores)
    if place != -1:
        for x in range(10, place, -1):
            scores[x] = scores[x - 1]
        scores[place] = [name, points]
    return scores

print(add_highscore(101, 'Ankile', hs))