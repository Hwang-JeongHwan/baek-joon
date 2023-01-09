n = int(input())
m = n
array = [500, 100, 50, 10]
count = 0
i = 0
while n > 0:
    count += n // array[i]
    n = n % array[i]
    i += 1

print(count)
count1 = 0
for coin in array:
    count1 += m // coin
    m %= coin

print(count1)

# 화폐의 종류가 K라고 할 때, 시간복잡도는 O(K)임
# 이 알고리즘의 시간 복잡도는 거슬러줘야 하는 금액과는 무관하며, 동전의 총 종류에만 영향을 받음 