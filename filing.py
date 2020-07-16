import pickle


def save(object, path):
    file = open(path, 'wb')
    pickle.dump(object, file)
    file.close()


def load(path):
    file = open(path, 'rb')
    cl = pickle.load(file)
    file.close()
    return cl
