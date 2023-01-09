# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5PzOCKAigDFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part2&problemBoxCnt=14

tc = int(input())
for t in range(1, tc + 1):
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    # print(graph[2][2])

    result = 0
    # for i in range(n - 1):
    #     index = 0
    #     for j in range(n - m + 1):
    #         up = sum(graph[i][j : m + index])
    #         down = sum(graph[i + 1][j :m + index])
    #         print(up, down)
    #         total = up + down
    for i in range(n - m + 1):
        index = 0
        for j in range(n - m + 1):
            total = 0
            for k in range(m):
                total += sum(graph[i + k][j :m + index])
            index += 1
            result = max(total, result)

    print('#{} {}'.format(t, result))