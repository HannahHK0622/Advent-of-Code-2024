from collections import Counter

with open("input 1.txt", "r") as text:
    nums = [int(x) for x in text.read().split()]
    set1 = nums[::2]
    set2 = nums[1::2]

set1.sort()
set2.sort()

diff = 0
diff_score = 0
for elem in range(len(set1)):
    current_no = set1[elem]
    diff += abs(set1[elem]-set2[elem])
    
set2_count = Counter(set2)
print(set2_count)
for number in set1:
    diff_score += number * set2_count[number]
print(f"The difference is {diff}")
print(f"The diff score is {diff_score}")

