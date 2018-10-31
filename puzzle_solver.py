import numpy as np

def solve_puzzle(puzzle, puzzleSize, dict, hor_word_starting, vert_word_starting, hor_length, vert_length, number_of_fields, hor_word):
    while hor_word < len(hor_word_starting):
        tempdict = (x for x in dict if len(x) == hor_length[hor_word])

        for word in tempdict:
            puzzle2 = np.copy(puzzle)
            puzzle2 = insert_word(puzzle2, word, hor_word_starting[hor_word], len(word), 0)
            number_of_fields -= hor_length[hor_word]
            if(check_if_valid(puzzle2, vert_word_starting, vert_length, number_of_fields, dict)):
                exit_function(puzzle2, puzzleSize)
            if(check_if_partial_valid(puzzle2, vert_word_starting, vert_length, dict) or hor_word == 0):
                solve_puzzle(puzzle2, puzzleSize, dict, hor_word_starting, vert_word_starting, hor_length, vert_length, number_of_fields, hor_word+1)


            number_of_fields += hor_length[hor_word]
        return "NO"











def check_if_valid(puzzle, vert_word_starting, vert_length, number_of_fields, dict):
    if number_of_fields != 0:
        return False
    elif check_if_partial_valid(puzzle,vert_word_starting, vert_length, dict):
        return True
    return False


def check_if_partial_valid(puzzle, vert_word_starting, vert_length, dict):
    word_num = 0
    for vert_word in vert_word_starting:
        x,y = vert_word
        if puzzle[x,y] != "_":
            if(check_vertical(puzzle,x,y,vert_length[word_num],dict) == False):
                return False
        word_num += 1
    return True
def insert_word(puzzle, word, word_start, word_length, dir):
    if dir == 0:
        for i in range(word_start[1], word_start[1]+word_length):
            puzzle[word_start[0],i] = word[i - word_start[1]]
    if dir == 1:
        for i in range(word_start[0], word_start[0]+word_length):
            puzzle[i,word_start[1]] = word[i-word_start[0]]

    return puzzle

def analyze_crossword(puzzle, puzzleSize):
    hor_word_starting = []
    vert_word_starting = []
    hor_length = []
    vert_length = []
    row = 0
    col = 0
    while row < puzzleSize:
        while col < puzzleSize:
            if puzzle[row, col] == "#":
                col += 1
                continue
            if puzzle[row, col] == "_":
                hor_word_starting.append([row,col])
                length = calculate_length_horizontally(puzzle, row, col, puzzleSize)
                col += length
                hor_length.append(length)
                continue
        col = 0
        row += 1

    row = 0
    col = 0

    while col < puzzleSize:
        while row < puzzleSize:
            if puzzle[row, col] == "#":
                row += 1
                continue
            if puzzle[row, col] == "_":
                vert_word_starting.append([row, col])
                length = calculate_length_vertically(puzzle, row, col, puzzleSize)
                row += length
                vert_length.append(length)
                continue
        row = 0
        col += 1

    number_of_fields = sum(hor_length)
    if not hor_word_starting or not vert_word_starting:
        return "NO", "NO","NO", "NO", "NO"
    else:
        return hor_word_starting, vert_word_starting, hor_length, vert_length, number_of_fields
def calculate_length_horizontally(puzzle, row, col, puzzleSize):
    length = 1
    for i in range(col+1,puzzleSize):
        if puzzle[row, i] == "#" or i == puzzleSize:
            return length
        else:
            length += 1
    return length
def calculate_length_vertically(puzzle, row, col, puzzleSize):
    length = 1
    for i in range(row + 1, puzzleSize):
        if puzzle[i, col] == "#" or i == puzzleSize:
            return length
        else:
            length += 1
    return length
def check_vertical(puzzle, x,y, length, dict):
    str = ""
    tempdict = (x for x in dict if len(x) == length)
    for i in range(x, x+length):
        if puzzle[i,y] == "#" or puzzle[i,y] == "_":
            break
        str += puzzle[i,y]

    for word in tempdict:
        if word.startswith(str):
            return True

    return False
def exit_function(puzzle, puzzleSize):
    str = ""
    for i in range(0, puzzleSize):
        for j in range(0, puzzleSize):
            str += puzzle[i, j]
            if (j != puzzleSize - 1):
                str += ";"
        str += '\n'
    print(str)
    exit();
