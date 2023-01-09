# 0에서 1로 변경하거나 1에서 0으로 변경하는 경우를 확인
# 전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중에서 더 적은 획수를 가지는 경우를 계산하면됨 
data = input()

count0 = 0 # 전부 0으로 바뀌는 경우
count1 = 0 # 전부 1로 바뀌는 경우 
if data[0] == '1':
    count0 += 1

else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i + 1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1

print(min(count0,count1))