n, m = map(int, input().split())
INF = int(1e9)

#노드의 개수 + 1 만큼 2차원리스트 만들어줌 
graph = [[INF] * (n + 1)for i in range(n + 1)]
# print(graph)

# 자기자신으로 가는경로는 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
# 각 간선에 대한 정보를 입력받아, 그값으로 초기화

# a,b는 연결되어있고 연결된 도로를 통해 a-> b , b->a로 가는 시간은 1임
for i in range(m):
    # A와 B가 서로에게 가는 비용은 1이라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# min(graph[a][b],graph[a][k]+graph[k][b])
# 점화식에 따라 플로이드 워셜 알고리즘을 수행 
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
# 거쳐갈 노드와 x와 최종 목적기 노드 K 를 입력받기 
x, k = map(int, input().split())

# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         if graph[a][b] == INF:
#             print(INF)
#         else:
#             print(graph[a][b], end = " ")
#     print()

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]
# print(graph)
# print(graph[1][k],'+',graph[k][x])
# 도달할 수 없는 경우, -1 을 출력
if distance >= INF:
    print("-1")
# 도달할 수 있다면, 최단거리 출력 
else:
    print(distance)
    