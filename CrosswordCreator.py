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

def checkColumnsValidity(words):
    crossword = [['#', 'a', 'b'], ['c', 'a', 'b'], ['a', '#', 'a']]
    crosswordSize = len(crossword)
    columnStrings = []
    for i in range(crosswordSize):
        columnValues = []
        for k in range(crosswordSize):
            cellValue = crossword[k][i]
            if (cellValue is not None):
                columnValues.append(cellValue)
        separateStrings = (''.join(columnValues)).split('#')
        columnStrings.append(separateStrings)
    print('Column strings', columnStrings)
    for i in range(len(columnStrings)):
        for k in range(len(columnStrings[i])):
            if (columnStrings[i][k] is '' or columnStrings[i][k] in words):
                print(columnStrings[i][k])
            else:
                return False
    return True

def putWordsInRows(crossword, words):
    wordsCopy = [x for x in words]
    rowsWords = [[] for x in range(len(crossword))]
    for i in range(len(crossword)):
        words = []
        for k in range(len(crossword)):
            if (crossword[i][k] is not '#'):
                words.append(crossword[i][k])
            else:
                rowsWords[i].append(words)
                words = []
        rowsWords[i].append(words)

    filledCrossword = [[] for x in range(len(crossword))]
    for i in range(len(rowsWords)):
        for k in range(len(rowsWords[i])):
            worldLength = len(rowsWords[i][k])
            if worldLength > 0:
                for x in range(len(wordsCopy)):
                    if (len(wordsCopy[x]) is worldLength):
                        pickedWord = wordsCopy.pop(x)
                        filledCrossword[i].append(pickedWord)
                        break
    print('Filled', filledCrossword)


if __name__ == '__main__':
    print('Starting CrosswordCreator')
    (words, layout) = decode()
    print('\nLayout: ', layout)
    print('Words: ', words)
    crossword = parseLayout(layout)
    columnsValid = checkColumnsValidity(words)
    putWordsInRows(crossword, words)
    print('Are columns valid?', columnsValid)



