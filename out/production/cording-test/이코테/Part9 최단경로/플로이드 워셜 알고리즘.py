# 노드의 개수가 500개 이하면 사용
# 노드의 개수가 500개가 된다고 해도 이 마저도 시간제한이 넉넉하지 않으면 시간초과
# 문제마다 적절한 알고리즘을 골라서 해결해야함 
INF = int(1e9) # 무한임을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기

n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)를 만들고, 무한으로 초기화

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# print(graph)

# 자기 자신에서 자기 자신으로 가는 비용은 0 으로 초기화
for a in range(1, n + 1):
    for b in range(1,n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    # 2차원 리스트에 바로 비용에대한 정보 기록 
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 실행
for k in range(1,n + 1): # k = 거쳐가는 노드
    for a in range(1, n + 1): # a = 출발노드
        for b in range(1, n + 1): # b = 도착노드
            # 최단 거리 = 기존의값과 a에서 k로 갓다가 k 에서 b로 가는값을 더한 값과비교해서 작은값
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우,무한(INFINITY)이라고 출력
        if graph[a][b] == INF:
            print("INFINITY")
        else:
            print(graph[a][b],end=" ")
    print()

