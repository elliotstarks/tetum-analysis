# Source code for getting usable tuples of data out of the dictionaries


def readParulDict(path):
    f = open(path, "r")
    pairings = []
    for line in f:
        line.translate(None, ';\n') #strips silly characters
        str_list = line.split()
        if len(str_list) > 1:
            pairings.append(str_list)
    f.close()
    return pairings

