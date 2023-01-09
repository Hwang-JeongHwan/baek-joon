# 위상 정렬은 DAG에 대해서만 수행할 수 있습니다.
# DAT(Direct Acyclic Graph): 순환하지 않는 방향 그래프

# 위상 정렬에서는 여러가지 잡이 존재할 수 있습니다.
# 한 단계에서 큐에 새롭게 들어가는 원소가 2개 이상인 경우가 있다면 여러가지 답이 존재합니다

# 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단할 수 있습니다.
# 사이클에 포함된 원소 중에서 어떠한 원소도 큐에 들어가지 못합니다.

# 스택을 활용한 DFS를 이용해 위상정렬을 수행할 수도 있습니다.
from collections import deque

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기 = 나가는 간선 제거 
    
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    # 위상 정렬 수행한 결과를 출력
    for i in result:
        print(i, end=' ')
# 노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())

# 모든 노드에 대해 진입차수는 0 으로 초기화
indegree = [0] * (v + 1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 정점 B로 이동 가능
    # 진입차수를 1 증가
    indegree[b] += 1

topology_sort()

# 위상정렬 알고리즘 성능 분석
# 위상 정렬을 위해 차례대로 모든 노드를 확인하며 각 노드에서 나가는 간선을 차례대로
# 제거 해야합니다.
# 위상정렬 알고리즘의 시간 복잡도는 O(V + E)입니다.
# 한번 큐에 들어간 노드는 다시한번 큐에 들어가지 않음 -> 한번 제거된 간선도 다시 제거
# 되지 않음 -> 그렇기 떄문에 전체 과정을 거치면서 각각의 노드와 그 노드에서 나가는
# 간선을 확인하기 때문에 위상정렬의 시간 복잡도는 O(V + E) 입니다.

