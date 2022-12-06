import heapq
n, m, start = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        
        dist, now = heapq.heappop(q)
        print(dist, now)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0
total = 0
# print(distance)
for i in range(1, n + 1):
    
    if distance[i] == INF or distance[i] == 0:
        continue
    
    if distance[i] > total:
        total = distance[i]
    count += 1
    
print(count, total)