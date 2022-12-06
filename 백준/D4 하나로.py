# 환경 부담금 = 환경부담 세율 (E) * 각 해저 터널의 길이(L)의 제곱의 곱
# (E * L ^ 2)

# x 기준으로 정렬했을때와
# y 를 기준으로 정렬했을때의 최소 스패닝 트리를 구하고 더 적은값 출력
def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    ix = list(map(int, input().split()))
    iy = list(map(int, input().split()))
    # x = []
    # y = []
    # for i in range(n):
    #     x.append((ix[i], i))
    #     y.append((iy[i], i))

    e = float(input())
    # x.sort()
    # y.sort()

    # print(x)
    # print(y)
    parent = [0] * n
    for i in range(n):
        parent[i] = i
    edges = []
    for i in range(n - 1):
        # 간선에 x좌표기준 거리 y좌표 기준 거리
        for j in range(i + 1, n):
            edges.append(((ix[i] - ix[j]) ** 2 + (iy[i] - iy[j]) ** 2, i, j))
            

    edges.sort()
    # print(edges)
    result = 0
    for edge in edges:
        cost, x, y = edge
        x = find_parent(parent, x)
        y = find_parent(parent, y)
        if x != y:
            union_parent(parent, x, y)
            result += (e * cost)

    print('#{} {}'.format(t, round(result)))
    # 10
    # 2
    # 0
    # 0
    # 0
    # 100
    # 1.0
    # 4
    # 0
    # 0
    # 400
    # 400
    # 0
    # 100
    # 0
    # 100
    # 1.0
    # 6
    # 0
    # 0
    # 400
    # 400
    # 1000
    # 2000
    # 0
    # 100
    # 0
    # 100
    # 600
    # 2000
    # 0.3
    # 9
    # 567
    # 5
    # 45674
    # 24
    # 797
    # 29
    # 0
    # 0
    # 0
    # 345352
    # 5464
    # 145346
    # 54764
    # 5875
    # 0
    # 3453
    # 4545
    # 123
    # 0.0005



# tc = int(input())
# for t in range(1, tc + 1):
#     n = int(input())
    # data = []
    #
    # for i in range(2):
    #     if i == 0:
    #         a = list(map(int, input().split()))
    #     else:
    #         b = list(map(int, input().split()))
    # print(a, b)
    # for i in range(n):
    #     data.append((a[i], b[i], i))
    # e = float(input())
    # print(data)
    # x = sorted(data, key = lambda x:(x[0] , x[1]))
    # y = sorted(data, key = lambda y: (y[1], y[0]))
    # print(x)
    # print(y)
    # parentx = [0] * (n)
    # parenty = [0] * (n)
    # for i in range(n):
    #     parentx[i] = i
    #     parenty[i] = i
    #
    # totalx = 0
    # totaly = 0
    # for i in range(n - 1):
    #     cost_x = abs(x[i][0] - x[i + 1][0]) + abs(x[i][1] - x[i + 1][1])
    #     cost_y = abs(y[i][0]- y[i + 1][0]) + abs(y[i][1] - y[i + 1][1])
    #     xa = find_parent(parentx, x[i][2])
    #     xb = find_parent(parentx, x[i + 1][2])
    #     ya = find_parent(parenty, y[i][2])
    #     yb = find_parent(parentx, y[i + 1][2])
    #     if xa != xb:
    #         union_parent(parentx, xa, xb)
    #         totalx += (e * (cost_x ** 2))
    #
    #     if ya != yb:
    #         union_parent(parenty, ya, yb)
    #         totaly += (e * (cost_y ** 2))
    #
    #
    # print(totalx, totaly)