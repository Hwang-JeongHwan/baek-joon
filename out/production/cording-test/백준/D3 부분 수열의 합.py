from itertools import combinations
tc = int(input())
for t in range(1, tc + 1):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    count = 0
    for i in range(1, n + 1):
        for combi in combinations(data, i):
            if sum(combi) == m:
                count += 1
    print('#{} {}'.format(t, count))
