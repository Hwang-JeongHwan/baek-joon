# 왼쪽부터 차례대로 식량창고를 턴다고 했을 때, 특정한 i번째 식량창고에 대해서
# 털지 안털지의 여부를 결정하면 , 아래 2가지 경우중 더 많은 식량을 털 수 있는 경우를
# 선택하면됨  i번째 창고는 i - 2 번째의 최적의 해와 i - 1번째의 최적의 해를 고려해서
# i + i - 2를 할지 i - 1을 선택할지 고르면됨 
# 최적 부분구조 = 특정 번째 까지의 최적의 해는 i - 2번째와 i - 1 번째를 확인
# 해서 계산되는것을 볼수있음 , 큰문제를 해결하기  위해 작은 문제 2가지를 고려 


import sys
input = sys.stdin.readline

n = int(input())

array = list(map(int, input().split()))
d = [0] * 100

d[0] = array[0]
d[1] = (max(array[0], array[1]))
for i in range(2, n):
    d[i] = max(array[i] + d[i - 2], d[i - 1])

print(d[n - 1])
