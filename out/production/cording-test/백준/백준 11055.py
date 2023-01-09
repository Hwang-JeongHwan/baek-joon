# https://www.acmicpc.net/problem/11055



n = int(input())
data = list(map(int, input().split()))

d = [0] * n
for i in range(n):
    d[i] = data[i]

result = 0
for i in range(1, n):
    total = 0
    for j in range(i):
        if data[i] > data[j]:
            d[i] = max(d[i], d[j] + data[i])


print(max(d))
