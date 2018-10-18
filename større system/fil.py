import pickle


def save(dictionary, filnavn):
    f = open(filnavn, 'bw')  # Åpner filen for binærskriving
    pickle.dump(dictionary, f)  # Dumper dictionary til fil
    f.close()


def load(filnavn):
    f = open(filnavn, 'br')
    dictionary = pickle.load(f)  # Last inn fil som dictionary
    f.close()
    return dictionary
