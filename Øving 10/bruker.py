def print_meny():
    None


def print_board(board):
    for row in board:
        print(row)



def check_input(user_input):
    if user_input.isdigit():
        if 1 <= int(user_input) <= 9:
            return True
    print('Kun tall mellom 1 og 9 er innafor.')
    return False


def generate_empty_board():
    return [[[[0 for i in range(3)] for i in range(3)] for i in range(3)] for i in range(3)]


print_board(generate_empty_board())