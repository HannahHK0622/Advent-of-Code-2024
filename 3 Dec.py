"""Solutions for Advent of Code 2024 Day 3"""

__author__ = "Hannah Kan"
import re as regex
from typing import List, Tuple


FILE_NAME = "input 3.txt"
MUL_PATTERN = regex.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)")
TEST_SNIPPET = "ho()who()$mul(990,670)-<mul(187,242) mul(643,672)&?;mul(935,319);"


def find_valid_muls(string: str) -> List[str]:
   return regex.findall(MUL_PATTERN, string)

   
def mul(operands: Tuple[int, int]) -> int:
    return operands[0] * operands[1]


def main():
    part_1_sumproduct: int = 0
    part_2_sumproduct: int = 0
    with open(FILE_NAME, "r") as f:
        bad_mem: str = f.read()
    operands: List[Tuple[int, int]] = build_list_of_muls(bad_mem)
    for operand_pair in operands:
        part_1_sumproduct += mul(operand_pair)
    print(f"part 1: {part_1_sumproduct}")
    
    slice_by_disabled: List[str] = \
        (["", bad_mem.split("don't()")[0]] #Accounting for implicit do() in the start
        + [substr[1:].split('do()') for substr in bad_mem.split("don't()")[1:]] )
    find_enabled: List[str] = ["".join(string[1:]) if len(string) >= 2 else "" for string in slice_by_disabled]
    
    
    enabled_muls: List[Tuple[int, int]] = build_list_of_muls("".join(find_enabled))
    for operand_pair in enabled_muls:
        part_2_sumproduct += mul(operand_pair)
    print(f"part 2: {part_2_sumproduct}")


def build_list_of_muls(bad_mem) -> List[tuple[int, int]]:
    return [tuple(int(num) for num in args[4:-1].split(',')) for args in find_valid_muls(bad_mem)]
    
    
if __name__ == "__main__":
    main()