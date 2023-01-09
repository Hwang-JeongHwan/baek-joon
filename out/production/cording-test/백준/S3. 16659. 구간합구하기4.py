import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
prefix_sum = [0] * (n + 1)
temp = 0
for i in range(n):
    temp += data[i]
    prefix_sum[i + 1] = temp
for _ in range(m):
    x, y = map(int, input().split())
    print(prefix_sum[y] - prefix_sum[x - 1])
    