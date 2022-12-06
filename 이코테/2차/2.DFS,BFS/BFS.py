# BFS는 너비 우선 탐색이라고도 부르며 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘임
# BFS는 큐 자료구조를 이용하며 구체적인 동작과정은 다음과 같음

# 1. 탐색 시작 노드를 큐에 삽입하고 방문처리를 함
# 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접노드중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
# 특정조건에서의 최단경로 알고리즘
# 3. 더이상 2번의 과정을 수행할수 없을때까지 반복
# 시작노드부터 가까운 노드부터 방문함
# 각 간선의 비용이 동일한 경우 최단거리를 구하기 위해 사용됨 

from collections import deque

def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append(start)
    # 큐에 시작노드를 집어넣어 놓고 시작
    # 현재 노드를 방문처리
    visited[start] = True
    # 큐가 빌때 까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS함수 호출

bfs(graph, 1, visited)