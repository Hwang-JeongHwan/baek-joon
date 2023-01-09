for tc in range(1, 11):
    t = int(input())
    data = []
    for _ in range(t):
        data.append(list(map(int, input().split())))
    count = 0
    result = []
    #print(result)
    for i in range(t):
        before = data[0][i]
        for j in range(t):
            if data[j][i] == 0:
                continue
            if before == 1 and data[j][i] == 2:
                count += 1
            before = data[j][i]





    print('#{} {}'.format(tc, count))

