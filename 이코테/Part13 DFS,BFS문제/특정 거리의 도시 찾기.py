# 모든 도로의 거리는 1이라는 조건 덕분에 너비 우선 탐색을 이용해 간단히 해결 가능
from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 벚ㄴ호

n, m ,k, x = map(int,input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출반 도시 까지의 거리는 0으로 설정

q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)
# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)