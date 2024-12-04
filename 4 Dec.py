"""Solutions to Advent of Code 2024 Day 4"""

__author__ = "Hannah Kan"

from typing import List
from numpy import array

FILE_NAME = "input 4.txt"

def transpose_crossword(crossword: List[str]) -> List[str]:
    x = [list(line.strip()) for line in crossword]
    transposed = [''.join(row) for row in zip(*x)]
    assert transposed != crossword
    return transposed

def all_indices(search_from: str, target: str) -> List[int]:
    return [index for index, letter in enumerate(search_from) if letter == target]

def count_diagonal_xmas(crosswords):
    count = 0
    for index, line in enumerate(crosswords):
        indices_of_x = all_indices(line, "X")
        for line_index in indices_of_x:
            try:
                #X...
                #.M..
                #..A.
                #...S
                if (crosswords[index+1][line_index+1] == "M"
                    and crosswords[index+2][line_index+2] == "A"
                    and crosswords[index+3][line_index+3] == "S"):
                    count += 1
                #...X
                #..M.
                #.A..
                #S...
                elif (crosswords[index+1][line_index-1] == "M"
                     and crosswords[index+2][line_index-2] == "A"
                     and crosswords[index+3][line_index] == "S"):
                    count += 1
                #...S
                #..A.
                #.M..
                #X...
                elif (crosswords[index-1][line_index+1] == "M"
                     and crosswords[index-2][line_index+2] == "A"
                     and crosswords[index-3][line_index+3] == "S"):
                    count += 1
                #S...
                #.A..
                #..M.
                #...X
                elif (crosswords[index-1][line_index-1] == "M"
                     and crosswords[index-2][line_index-2] == "A"
                     and crosswords[index-3][line_index-3] == "S"):
                    count += 1
            except IndexError:
                pass
    return count

def all_indices(string, char):
    return [i for i, c in enumerate(string) if c == char]
def main():
    tally: int = 0
    with open(FILE_NAME, "r") as f:
        crosswords: List[str] = f.readlines()
    
    for line in crosswords:
        tally += line.count("XMAS") + line.count("SAMX") # Trivial case when the 'XMAS' is in one line
    
    for line in transpose_crossword(crosswords):
        tally += line.count("XMAS") + line.count("SAMX")
    try:
        tally += count_diagonal_xmas(crosswords)
    except IndexError:
        pass
    
    print(tally)

if __name__ == "__main__":
    main()