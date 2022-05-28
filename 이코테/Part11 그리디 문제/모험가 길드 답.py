n = int(input())
# 3 1 1 1 1
data = list(map(int, input().split()))
# 오름차순으로 정렬
# 1 1 1 1 3
data.sort()
result = 0
count = 0

for i in data: 
    # 1. i = 1  2. i = 1 3. i = 1  4. i = 1 5. i = 3 
    count += 1
    # 1. count = 1, i = 1 2. count = 1, i = 1 3. count = 1, i = 1 4. count = 1, i = 1 5. i= 3, count = 1
    if count >= i:
        result += 1
        count = 0
# result = 4
# 모든 모험가가 그룹에 있을 필요 x , 마을에 남은 모험가가 있어도됨 
print(result)