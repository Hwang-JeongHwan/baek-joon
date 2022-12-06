n = int(input())
array = []
dp = [[0] * n for _ in range(n)]
for i in range(n):
    array.append((list(map(int, input().split()))))



for i in range(1, n):
    for j in range(i + 1):
        # (i - 1, j) (i - 1, j -1)
        # print(i, j)
        if j == 0:
            left = 0
        else:
            left = array[i - 1][j - 1]
        if j == i:
            right = 0
        else:
            right = array[i - 1][j]

        array[i][j] = array[i][j] + max(left, right)

result = 0
for i in range(n):
    max_num = max(array[i])
    result = max(max_num, result) 
# print(array)
print(result)