import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

home = []
chickens = []
for i in range(n):
    data = list(map(int, input().split()))
    #print(len(data))
    for j in range(len(data)):
        if data[j] == 1:
            home.append((i, j))
        if data[j] == 2:
            chickens.append((i, j))

def get_sum(candidate):
    result = 0
    for hx, hy in home:
        total = int(1e9)
    
        for cx, cy in candidate:
            total = min(total, abs(hx - cx) + abs(hy - cy))
        result += total
    return result

#candidates = combinations(chickens, m)
# result = int(1e9)
# for candidate in combinations(chickens, m):
#     result = min(result, get_sum(candidate))
# print(result)


result = int(1e9)
for candidate in combinations(chickens, m):
    total = 0
    for hx, hy in home:
        distance = int(1e9)
        for cx, cy in candidate:
            distance = min(distance, abs(hx - cx) + abs(hy - cy))
        total += distance
    result = min(total, result)

print(result)

