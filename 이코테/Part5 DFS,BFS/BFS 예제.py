from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌때 까지 반복

    while queue:
        # 큐에서 한의 원소를 뽑아 추출하기
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                print(queue)


# 각 노드가 연결된 정보를 표현 (2차원 리스트)
# 노드의 번호가 1번부터 시작하는 경우가 많아 0번은 비워두는게 좋다고함

x = deque([1])
print(x)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
# 모든값을 False값으로 초기화 해서 처음에는 모든 노드를 방문하지 않은것처럼 초기화
# index0 은 사용하지 않기 위해 하나더 큰 크기로 초기화 함

print(graph)
visited = [False] * 9

bfs(graph, 1, visited)
