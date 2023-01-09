import sys
import heapq
input = sys.stdin.readline

n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]
print(graph)
INF = int(1e9)

distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미 
# 1 2 4 , 1 3 2
# [[(2, 4),(3, 2)]]
print(graph)

def dijkstra(start):
    
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기

        dist, now = heapq.heappop(q)
        
        # 현재 노드가 이미 처리 됐다면 무시
        
        # 모든 거리는 무한대로 초기화 한 상태, start만 0으로 초기화 즉 한번이라도 처리됏다면
        # distance[now] < dist임
        # 이미 더 짧은 거리가 기록되어있다면 확인할 필요가 없음  
        if distance[now] < dist:
            continue
        # 현재노드와 연결된 다른 인접노드를 확인 
        
        # cost값이 인접노드에 대한 거리값보다 작은경우 작은 값으로 갱신 
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 디른 노드로 이동하는 거리가 더 짧은경우

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0
max_distance = 0

for d in distance:
    if d != INF:
        count +=1
        max_distance = max(max_distance,d)
# 시작 노드는 제외해야 하므로 count - 1을 출력

print(count - 1,max_distance)