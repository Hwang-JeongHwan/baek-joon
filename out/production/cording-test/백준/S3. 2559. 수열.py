# 3 -2 -4 9 0 3 7 13 8
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

temp = 0
result = [sum(data[ : k])]
for i in range(n - k):
    result.append(result[i] - data[i] + data[i + k])
print(max(result))
    