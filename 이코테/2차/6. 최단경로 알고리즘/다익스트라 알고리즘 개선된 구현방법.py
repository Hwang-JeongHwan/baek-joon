# 단계마다 방문하지 않은 노드중에서 최단거리가 가장 짧은 노드를 선택하기 위해
# 힙(Heap) 자료구조를 이용함

# 다익스트라 알고리즘이 동작하는 기본 원리는 동일함
# 현재 가장 가까운 노드를 저장해 놓기 위해서 힙 자료구조를 추가적으로 이용한다는 점이 다름
# 현재의 최단 거리가 가장 짧은 노드를 선택해야 하므로 최소 힙을 사용함

# 거리를 앞으로 집어넣어야할듯?

# 갱신된 노드만 다시 우선순위 큐에 넣어줌
# 이미 방문했으면 무시

# 우선순위 큐에서 꺼낸 값이 현재 테이블에 있는 값보다 크면 무시
# 이동할수있는 인접노드, 간선이 없으면 테이블이 갱신되지 않고 우선순위큐도 변동이 없음


# 가장 짧은 최단거리 노드를 찾는 함수 필요x 
# 힙에 저장할때 비용순으로 넣기 때문에  거리가 가장 짧은 노드부터 나옴 
# visted(방문여부)리스트도 필요없음 dist 와 distance[now] 를 비교해서
# distance[now] < dist: continue
# 
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
start = int(input())
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        # 거리가 더 크면 이미 처리가 되었다는 뜻임
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                # 갱신후 우선순위 큐에 넣어줌 
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print('infinity')
    else:
        print(distance[i])
        
# 개선된 구현 방법 성능분석
# 힙 자료 구조를 이용하는 다익스트라 알고리즘의 시간복잡도는 O(ElogV) E는 간선 V는 노드
# 노드를 하나씩 꺼내 검사하는 반복문은 노드의 개수 V이상의 횟수로는 처리되지 않음
# 결과적으로 현재 우선순위 큐에서 꺼낸 노드와 연결된 다른 노드들을 확인하는 총 횟수는
# 최대 간선의 개수 E 만큼 연산이 수행될 수 있음
# 직관적으로 전체 과정은 E개의 원소를 우선순위 큐에 넣었다가 모두 빼내는 연산과
# 매우 유사함
# 
# 시간 복잡도를 O(ElogE)로 판단할수 있고 
# 중복 간선을 포함 하지않는 경우에 이를 O(ElogV)로 정리할수있음 
