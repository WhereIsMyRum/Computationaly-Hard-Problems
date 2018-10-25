from Decoding import decode

def parseLayout(layout):
    crosswordSize = len(layout)
    crossword = [[] for x in range(crosswordSize)]
    for i in range(crosswordSize):
        cleanLayoutLine = layout[i].replace(';','')
        for k in range(len(cleanLayoutLine)):
            if (cleanLayoutLine[k] is '#'):
                crossword[i].append(cleanLayoutLine[k])
            else:
                crossword[i].append(None)
    print('Parsed layout: ', crossword)
    return crossword

def computeFreeSpaces(crossword):
    crosswordSize = len(crossword)
    rows = []
    columns = []
    for i in range(crosswordSize):
        for k in range(len(crossword[i])):
            pass


if __name__ == '__main__':
    print('Starting CrosswordCreator')
    (words, layout) = decode()
    print(words, layout)
    crossword = parseLayout(layout)


