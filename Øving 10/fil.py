import pickle


def save(filename, board):
    f = open(filename, 'bw')
    pickle.dump(board, f)
    f.close()
    print('Brett lagret\n')



def load(filename):
    f = open(filename, 'br')
    board = pickle.load(f)
    f.close()
    print('Brett lastet\n')
    return board