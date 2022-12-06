import sys
from itertools import combinations

def find(array, start, end):
    total = 0
    while start <= end:
        mid = (start + end) // 2
        left_side = array[mid] - array[start]
        right_side = array[end] - array[mid]


        if left_side > right_side:
            more = right_side
            start = mid + 1
        else:
            more = left_side
            end = mid - 1
        total = max(more, total)
    return total
input = sys.stdin.readline

n, c = map(int, input().split())
data = []

for _ in range(n):
    data.append(int(input()))
# print(data)
data.sort()
result = 0
for combi in combinations(data, c):
    result = max(result, find(combi, 0, c - 1))

print(result)