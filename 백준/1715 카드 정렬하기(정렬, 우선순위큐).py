from collections import deque
import heapq

n = int(input())
data = []
for i in range(n):
    x = int(input())
    data.append(x)

data.sort()
# print(data)

heapq.heapify(data)
# print(data)
result = 0
while data:
    x = heapq.heappop(data)
    if len(data) == 0:
        break
    y = heapq.heappop(data)
    total = x + y
    result += total
    heapq.heappush(data, total)
print(result)

