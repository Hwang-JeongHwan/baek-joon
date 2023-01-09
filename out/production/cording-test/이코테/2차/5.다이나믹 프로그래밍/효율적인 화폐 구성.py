n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))

d = [1e9] * (m + 1)
for i in array:
    d[i] = 1

for i in range(1, m + 1):
    for j in array:
        d[i] = min(d[i], d[i - j] + 1)

if d[m] == 1e9:
    print(-1)
else:
    print(d)