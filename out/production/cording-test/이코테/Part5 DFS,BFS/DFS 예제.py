# DFS 메서드 정의
def dfs(graph, v, visited): # 그래프에 대한 정보, 방문처리 여부가 기록되어있는 리스트를 이용

    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end =' ')
    # 현재 노드(즉 스택의 최상단의 원소)와 연결된 다른 노드(인접한 노드)를 재귀적으로 방문
    for i in graph[v]:
        print('i',i)
        if not visited[i]: 
            # visited[i]가 False면
            dfs(graph, i , visited)


#각 노드가 연결된 정보를 표현 (2차원 리스트)
# 노드의 번호가 1번부터 시작하는 경우가 많아 0번은 비워두는게 좋다고함

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

dfs(graph, 1, visited)
