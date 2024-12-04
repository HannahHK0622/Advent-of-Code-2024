"""Solutions for Advent of Code 2024 Day 2"""

__author__ = "Hannah Kan"

from typing import List

FILE_NAME = "input 2.txt"

def find_diff(report: List[int]) -> List[int]:
    diffs = [0 for number in report[1:]]
    for i in range(len(report)-1):
        diffs[i] = report[i] - report[i+1]
    return diffs

def check_safety_q1(report: List[int]) -> bool:
    diffs = find_diff(report)
    if(all(abs(diff) <= 3 for diff in diffs)): # if each jump is <= 3
        if(all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs)): #If the sign of differences is all the same, and collorarily diff is not 0.   
            return True 
    return False

def check_safety_q2(report: List[int]) -> bool:
    q1_pass: int = check_safety_q1(report)
    if not q1_pass:
        problem_dampened_solutions: List[bool] = []
        for ignored in range(len(report)):
            problem_dampened_solutions.append(check_safety_q1(report[:ignored] + report[ignored+1:]))
    if(q1_pass or any(problem_dampened_solutions)):
        return True
    return False

def main() -> None:
    with open(FILE_NAME, "r") as f:
        inputs: List[List[int]] = [[int(num) for num in input] for input in [reading.split() for reading in f.read().split('\n')]]
        is_safe_q1: List[bool] = [check_safety_q1(input) for input in inputs]
        is_safe_q2: List[bool] = [check_safety_q2(input) for input in inputs]
        
    print(f'Q1: {is_safe_q1.count(True)}')
    print(f'Q2: {is_safe_q2.count(True)}')

if __name__ == "__main__":
    main()