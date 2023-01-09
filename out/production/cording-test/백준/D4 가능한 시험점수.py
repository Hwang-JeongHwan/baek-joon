# from itertools import combinations
#
# tc = int(input())
# for t in range(1, tc + 1):
#     n = int(input())
#     data = list(map(int, input().split()))
#     result = set()
#     result.add(0)
#     for i in range(1, n + 1):
#         total = 0
#         for combi in combinations(data, i):
#             total = sum(combi)
#             result.add(total)
#
#     print('#{} {}'.format(t, len(result)))
from itertools import combinations

tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    data = list(map(int, input().split()))
    visited = [0] * (sum(data) + 1)
    visited[0] = 1

    for i in range(n):
        for j in range(len(visited) - data[i], -1, -1):
            # print(j)
            if visited[j] == 1:
                visited[j + data[i]] = 1

    print('#{} {}'.format(t, sum(visited)))


# 2
# 3
# 2 3 5
# 10
# 1 1 1 1 1 1 1 1 1 1