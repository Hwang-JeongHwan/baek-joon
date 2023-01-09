# from itertools import combinations
#
# tc = int(input())
# answer = []
# for t in range(1, tc + 1):
#     n, k = map(int, input().split())
#     data = []
#     for i in range(n):
#         v, c = map(int, input().split())
#         data.append((v, c))
#     result = 0
#
#     for i in range(1, n + 1):
#         for combi in combinations(data, i):
#             vi = 0
#             ci = 0
#             for x, y in combi:
#                 vi += x
#                 ci += y
#
#             if vi <= k:
#                 result = max(result, ci)
#     answer.append(result)
#
#
# for t in range(tc):
#     print('#{} {}'.format(t + 1, answer[t]))


# n번 까지 선택했을때의 무게
# dp[n][w] = max(dp[n - 1][w], dp[n - 1][w - v[n - 1]] + c[n - 1])
# dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - [vi]] + c[i]) if vi <= w
# else dp[i][w] = dp[i - 1][w]


tc = int(input())

for t in range(1, tc + 1):
    n, k = map(int, input().split())
    data = []
    for i in range(n):
        v, c = map(int, input().split())
        data.append((v, c))

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if data[i - 1][0] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - data[i - 1][0]] + data[i - 1][1])
            else:
                dp[i][j] = dp[i - 1][j]
            # print(i,j, dp[i][j])
    print('#{} {}'.format(t, dp[n][k]))
