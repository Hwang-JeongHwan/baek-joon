tc = int(input())
# 1 과 2가 같은 복도를 사용하고 있으므로
# 1,2 를 같은 복도라고 생각
# 1,2 로 인덱싱 하면 어려우니까
# 1 - 1, 2 - 1 = (0, 1) 을 같은 공간이라고 생각하고 빈도수 check
# 0, 1 이 같아야하므로 0 // 2 = 1 // 2 = > 2로 나누어 줘서 같은공간이라고 생각

for t in range(1, tc + 1):
    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))

    count = [0] * (400 // 2)

    for i in range(n):

        start = data[i][0]
        end = data[i][1]
        if start > end:
            start, end = end, start

        for j in range((start - 1) // 2, (end - 1) // 2 + 1):
            # print(j)
            count[j] += 1
    result = max(count)
    print('#{} {}'.format(t, result))





# 3
# 4
# 10 20
# 30 40
# 50 60
# 70 80
# 2
# 1 3
# 2 200
# 3
# 10 100
# 20 80
# 30 50