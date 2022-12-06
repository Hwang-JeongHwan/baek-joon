# DFS는 깊이 우선 탐색이라고도 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘임
# DFS는 스택 자료구조 혹은 재귀함수를 이용하며, 구체적인 동작과정은 다음과 같음
# 1. 탐색 시작 노드를 스택에 삽입하고 방문처리를 함
# 2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리함
# 방문하지 않은 인접노드가 없으면 스택에서 최상단 노드를 꺼냄
# 매번 최상단의 원소를 기준으로 해서 방문하지 않은 인접노드가 있으면 그 인접한 노드로도 방문을 수행함


# 3. 더이상 2번의 과정을 수행할 수 없을 때까지 반복함

# dfs는 그래프의 정보 + 방문처리가 기록된 리스트를 이용! 
def dfs(graph, v, visited):
    # 현재 노드를 방문처리
    visited[v] = True
    # 방문했다는 표시로 현재 노드의 번호를 출력
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    # 인접한 노드가 방문되지 않은 상태라면 그 노드에 대해서도 마찬가지로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    print('pop',v)

# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [], # index 0에 대한 내용은 비워둠
    [2, 3, 8], # 1번노드부터 시작 
    [7], 
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]

]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)