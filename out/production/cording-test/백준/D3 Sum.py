# 가로 세로 대각선의 합중 최대값을 구하는 프로그램

tc = 10
for _ in range(1, tc + 1):
    t = int(input())
    data = []
    for i in range(100):
        data.append(list(map(int, input().split())))

    # print(len(data))
    # print(len(data[0]))
    row = 0
    column = 0
    cross = 0
    reverse = 0
    for i in range(100):
        row = max(row, sum(data[i]))
        c = 0
        for j in range(100):
            c += data[j][i]
            if i == j:
                cross += data[i][j]
            if j == 100 - i - 1:
                reverse += data[i][j]
        column = max(c, column)

    print('#{} {}'.format(t, max(row, column, cross, reverse)))
