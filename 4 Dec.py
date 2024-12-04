"""Solutions to Advent of Code 2024 Day 4"""

__author__ = "Hannah Kan"

from typing import List

FILE_NAME = "input 4.txt"

def count_diagonal_xmas(crosswords: List[str]) -> str:
    pass

def main():
    tally: int = 0
    with open(FILE_NAME, "r") as f:
        crosswords: List[str] = f.readlines()
    
    for line in crosswords:
        tally += line.count("XMAS") + line.count("SAMX") # Trivial case
    
    tally += count_diagonal_xmas(crosswords)

if __name__ == "__main__":
    main()