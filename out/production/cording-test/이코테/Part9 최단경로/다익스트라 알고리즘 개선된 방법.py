import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] *(n + 1)

# 모든 간선 정보를 입력받기

for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b 번 노드로 가는 비용이 c 라는 의미
    graph[a].append((b, c))
# print(graph)
# print(graph[1])
# x = graph[1]
# print (x[1])
# y = x[1]
# print('y',y)
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하며 큐에 삽입
    heapq.heappush(q,(0, start))
    distance[start] = 0
    while q: # 큐가 비어 있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        # dist 에는 튜플의 0번째 now에는 튜플의 두번째 정보가 들어감
        # 즉 dist에는 cost, now 에는 노드번호가 들어감 
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        # 즉 distance의 현재 노드의 거리가 힙안에서 꺼낸 거리값보다 적으면 
        # 더 크다면 업데이트 해야함 
        # 현재 꺼낸 원소의 거리값이 테이블에 기록된 값보다 더 크다면 이미 처리된것으로
        # 간주할수있음 -> 거리값을 비교해서 현재 꺼낸 거리값이 더 크다면 무시할수있도록함

        if distance[now] < dist : 
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        # i = graph[now]안의 원소 즉 now = 1이라면
        # 맨처음 i = (2, 2) -> i = (3, 5) -> i = (4, 1)
        # 두번째 원소는 거리값을 의미함 -> 현재 확인하고 있는 노드까지의 거리값에 그 노드와 인접한
        # 다른 노드의 거리값을 더한값을 cost에 담을수 있게 하고
         
        for i in graph[now]:
            #print('i=',i)
            cost = dist + i[1] 
            #print('i1 = ',i[1])
            # 여기서 i[1] = 튜플의 두번째 원소 (3, 5)면 5임 
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            # cost값이 인접노드에 대한 거리값보다 작은경우 작은 값으로 갱신 
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # 이렇게 값을 갱신할때마다 우선순위가 해당정보가 기록 될수있도록함 
                heapq.heappush(q, (cost, i[0]))
                # 여기서 i[0]은 노드 번호임
                
# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])

