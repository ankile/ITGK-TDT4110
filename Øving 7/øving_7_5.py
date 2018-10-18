facebook = [["Mark", "Zuckerberg", 32, "Male", "Married"],
            ["Therese", "Johaug", 28, "Female", "Complicated"],
            ["Mark", "Wahlberg", 45, "Male", "Married"],
            ["Siv", "Jensen", 47, "Female", "Single"]]


# a)
def add_data(user):
    list = user.split()
    list[2] = int(list[2])
    return list


print(add_data('Mark Zuckerberg 32 Male Married'))


# b)
def get_person(given_name, facebook):
    people = []
    for i in facebook:
        if given_name == i[0]:
            people.append(i)
    return people


print(get_person('Mark', facebook))

# c)
def main():
    print('Her kan du legge til brukere i fjesboka. Avslutt med "done".')

    while True:
        print('Legg inn ny bruker på formen ("given_name surname age gender relationship_status")')
        user = input()

        if user == 'done':
            break

        facebook.append(add_data(user))

    while True:
        print('Ønsker du søke etter en bruker? (avslutt med "done")')
        user = input()

        if user == 'done':
            break

        print(get_person(user, facebook))


main()