'''
문제설명
동빈이는 숨바꼭질을 하면서 술래로부터 잡히지 않도록 숨을 곳을 찾고 있다. 동빈이는 1 ~ N번까지의 헛간 중에서 하나를 골라 숨을 수 있으며, 술래는 항상 1번 헛간에서 출발한다. 전체 맵에는 총 M개의 양방향 통로가 존재하며, 하나의 통로는 서로 다른 두 헛간을 연결한다. 또한 전체 맵은 항상 어떤 헛간에서 다른 어떤 헛간으로 도달이 가능한 형태로 주어진다.

 

동빈이는 1번 헛간으로부터 최단 거리가 가장 먼 헛간이 가장 안전하다고 판단하고 있다. 이 때 최단 거리의 의미는 지나야 하는 길의 최소 개수를 의미한다. 동빈이가 숨을 헛간의 번호를 출력하는 프로그램을 작성해라.

입력조건
첫째 줄에는 N과 M이 주어지며, 공백으로 구분한다.(2 <= N <= 20,000), (1 <= M <= 50,000)
이후 M개의 줄에 걸쳐서 서로 연결된 두 헛간 A와 B의 번호가 공백으로 구분되어 주어진다.(1 <= A, B <= N)
출력조건
첫 번째는 숨어야 하는 헛간 번호를(만약 거리가 같은 헛간이 여러개면 가장 작은 헛간 번호를 출력한다.) 두 번째는 그 헛간까지의 거리를, 세 번째는 그 헛간과 같은 거리를 갖는 헛간의 개수를 출력해라.
'''
 
 # 술래는 항상 1번에서 출발
 # 양방향 통로
 # 1번으로부터 최단거리가 가장 먼곳이 가장 안전

import sys
import heapq
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            
            # print(graph[now], i)
            # print(i[0],i[1])
            # print(dist)
            # print(dist + i[1])
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
        

input = sys.stdin.readline
n, m  = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))
# print(graph)
distance = [INF] * (n + 1)
start = 1
dijkstra(1)
# print(distance)
max_value = max(distance[1:])
# print(max_value)
print(distance.index(max_value), max_value, distance.count(max_value))    
