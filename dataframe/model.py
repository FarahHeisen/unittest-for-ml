import pickle5 as pickle


def save_model(model, filename):
    file_out = open(filename, "wb")
    pickle.dump(model, file_out)
    file_out.close()
