#1초에 2000만번까지 연산가능 하면 괜찮음
# 24 * 60 * 60 = 86400 < 20000000
n = int(input())
count = 0
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함 되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)