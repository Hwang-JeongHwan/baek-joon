# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV13_BWKACUCFAYh&probBoxId=AV-HZfeqN3ADFASP&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part3&problemBoxCnt=14

# i == j
# j == n i == 0
# j == n - 1 i == 1

tc = 10
for t in range(1, tc + 1):
    n = int(input())
    data = []
    for _ in range(100):
        data.append(list(map(int, input().split())))
    
    cross = 0
    row = 0
    column = 0
    reverse = 0

    for i in range(100):
        x = 0
        y = 0
        k = 100 - i - 1
        # print(i, k)
        reverse += data[i][k]
        
        for j in range(100):
            if i == j :
                cross += data[i][j]
            x += data[i][j]
            y += data[j][i]
            # print(y)
        row = max(row, x)
        column = max(column, y)
    # print(row, column, cross, reverse)
    max_value = max(row, column, cross, reverse)
    print('#{} {}'.format(n, max_value))

            