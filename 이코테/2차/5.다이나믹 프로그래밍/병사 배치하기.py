# 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치
# 앞쪽에 있는 병사의 전투력이 항상 뛰쪽에 있는 병사보다 높아야함

n = int(input())
array = list(map(int, input().split()))
count = 0
if array[0] < array[1]:
    count += 1

for i in range(1, n - 1):
    if array[i] < array[i + 1] and array[i] < array[i - 1]:
        print(array[i])
        count += 1

print(count)