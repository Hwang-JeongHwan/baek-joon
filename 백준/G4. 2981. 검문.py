# 2부터 입력받는 수 중에 가장 작은수까지
import sys
input = sys.stdin.readline
n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

min_value = min(data)
result = []
for i in range(2, min_value):
    flag = True
    mod  = data[0] % i
    # print('mod',mod)
    for j in range(1, n):
        # print(data[j]%i)
        if mod != data[j] % i:
            flag = False
    if flag:
        result.append(i)

print(*result)