import sys

import numpy as np
from puzzle_solver import *


inputs = []

#reading input from a file
'''
with open("test01.CPC") as f:
    inputs = f.readlines()
inputs = [x.strip() for x in inputs if x]
inputs.append(" ")
'''


#reading input from stdin (for CodeJudge)

for line in sys.stdin:
    if str(line) != "":
        inputs.append(line)

inputs.append(" ")


if len(inputs) < 3:
    sys.stdout.write("NO")
    exit()

head = inputs[0].split(";")

if head[0] == "" or head[1] == "" or head[2] == "":
    sys.stdout.write("NO")
    exit()
alphLength = int(head[0])
dictLength = int(head[1])
puzzleSize = int(head[2])
if alphLength < 1 or dictLength < 1 or puzzleSize < 1:
    sys.stdout.write("NO")
    exit()

alphabet = inputs[1].split(";")
if np.unique(alphabet).size != len(alphabet) or len(alphabet) != alphLength:
    sys.stdout.write("NO")
    exit()

puzzle = []
for i in range(0, puzzleSize):
    input = inputs[i + 2].replace(" ", "")
    for j in range(0, puzzleSize + (puzzleSize - 1)):
        if input[j] != "#" and input[j] != "_" and input[j] != ";":
            sys.stdout.write("NO")
            exit()
        puzzle.append(input[j])

    puzzle.append("C")
if puzzle[0] != "#" and puzzle[0] != "_":
    sys.stdout.write("NO")
    exit()

for i in range(0, len(puzzle)):
    if puzzle[i] == "#" or puzzle[i] == "_":
        if puzzle[i + 1] == "#" or puzzle[i + 1] == "_":
            sys.stdout.write("NO")
            exit()

    if puzzle[i] == ";":
        if puzzle[i + 1] != "#" and puzzle[i + 1] != "_":
            sys.stdout.write("NO")
            exit()

puzzle = [x for x in puzzle if x != "C"]

dict = []
i = 2 + puzzleSize
while inputs[i] != " ":
    if inputs[i] == '\n' or inputs[i] == "#" or inputs[i] == "_" or inputs[i] == ";":
        sys.stdout.write("NO")
        exit()
    dict.append(inputs[i].rstrip())
    i = i + 1

if len(dict) != dictLength:
    sys.stdout.write("NO")
    exit()

#sys.stdout.write("YES")

dict.sort(key = lambda s: len(s))
dict2 = np.empty([puzzleSize,len(dict)])


#reshape the 1d array into 2d matrix and remove the ';'
puzzle2 = [x for x in puzzle if x != ";"]
puzzleMat = np.asmatrix(puzzle2).reshape((puzzleSize,puzzleSize))
hor_word_starting, vert_word_starting, hor_length, vert_length, number_of_fields = analyze_crossword(puzzleMat, puzzleSize)

if( hor_word_starting != "NO"):
    print(solve_puzzle(puzzleMat,puzzleSize,dict, hor_word_starting, vert_word_starting, hor_length, vert_length, number_of_fields, 0))

else:
    str = ""
    for i in range(0, puzzleSize):
        for j in range(0, puzzleSize):
            str += puzzleMat[i, j]
            if (j != puzzleSize - 1):
                str += ";"
        str += '\n'
    print(str)