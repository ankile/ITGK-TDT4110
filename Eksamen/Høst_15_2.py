NTNU_scores = (89, 77, 65, 53, 41, 0)
NTNU_letters = ('A', 'B', 'C', 'D', 'E', 'F')
TASKS = ('1', '2a', '2b', '2c', '3a', '3b', '3c', '3d', '4a', '4b', '4c', '4d', '4e', '4f', '4g', '4h')
WEIGHTS = tuple([25] + (15 * [5]))


def make_array(numbers, texts):
    outer_list = []
    for i in range(len(numbers)):
        outer_list.append([numbers[i], texts[i]])
    return outer_list


limit_letters = make_array(NTNU_scores, NTNU_letters)
weight_tasks = make_array(WEIGHTS, TASKS)


def compute_score(points, weights):
    min_sum = 0
    for i in range(len(points)):
        min_sum += points[i] * weights[i]

    return min_sum / 10


test = [4] * 16
test_2 = [10] * 5 + [0] * 11


# print(compute_score(test, WEIGHTS))

def score_2_letter(score_sum, limit_letters):
    for grade in limit_letters:
        if score_sum >= grade[0]:
            return grade[1]


# print(score_2_letter(89.9, limit_letters))

def add_candidate(candidate_number, scores, weights):
    new_line = str(candidate_number) + '\t'
    for score in scores:
        new_line += str(score) + '\t'
    new_line += str(compute_score(scores, weights)) + '\n'

    try:
        f = open('eksamen.txt', 'a')
        f.write(new_line)
        f.close()
    except Exception as error_message:
        print(error_message)


# add_candidate(11400, test, WEIGHTS)
# add_candidate(12300, test_2, WEIGHTS)

def read_result_file(filename):
    f = open(filename, 'r')
    content = f.readlines()
    f.close()

    for i in range(len(content)):
        content[i] = content[i].strip()
        content[i] = content[i].split('\t')
        for j in range(len(content[i])):
            if j != len(content[i]) - 1:
                content[i][j] = int(content[i][j])
            else:
                content[i][j] = float(content[i][j])

    return content


# print(read_result_file('eksamen.txt'))

def check_result_ok(filename, weights):
    # Load the file into a variable
    content = read_result_file(filename)

    all_ok = True
    # Candidate listed only once
    for i in range(len(content)):
        for j in range(i, len(content)):
            if content[i][0] == content[j][0] and i != j:
                all_ok = False
                print('ERROR: Candidate', content[i][0], 'appears more than once.')

    # No less than 0 or no more than 10 points per task
    for line in content:
        for i in range(1, len(line) - 1):
            if line[i] < 0 or line[i] > 10:
                all_ok = False
                print('ERROR: Candidate', line[0], 'scores are not between 0 and 10.')

    # Correct total
    for line in content:
        if compute_score(line[1:len(line) - 1], weights) != line[len(line) - 1]:
            all_ok = False
            print('ERROR: Candidate', line[0], 'has wrong total score.')

    return all_ok


# print(check_result_ok('eksamen.txt', WEIGHTS))

def list_all(filename, limit_letters):
    content = read_result_file(filename)
    content.sort()

    count = 0
    for line in content:
        letter = score_2_letter(line[len(line) - 1], limit_letters)
        print(line[0], end=' ')
        print(str((line[len(line) - 1])).rjust(5), end=' ')
        print(letter)
        count += 1

    return count


# print(list_all('eksamen.txt', limit_letters))

result = [] + ['string']

print(result)

ordbok = {}

ordbok['nøkkel'] = 100

print(ordbok)

alle_biler = ['enbil', 'tobil', 'trebil']

for bil in alle_biler:
    print(bil)
    bil = 0
    print(bil)
    
print(alle_biler)
