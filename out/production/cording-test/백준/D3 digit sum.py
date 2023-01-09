def dfs(s):
    if len(s) == 1:
        return s
    result = 0
    for i in range(len(s)):
        result += int(s[i])

    return dfs(str(result))


tc = int(input())
data = []
for t in range(1, tc + 1):
    n = input()
    data.append(n)

for t in range(tc):
    result = 0

    x = dfs(data[t])
    print('#{} {}'.format(t + 1, x))