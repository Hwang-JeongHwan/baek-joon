graph = []
# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    # print(x, y)
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문처리
        graph[x][y] = 1
        # 연결된 모든 위치에대해 방문처리를 진행하기 위해 
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        # 재귀적으로 호출후 True반환 결과적으로 True값을 반환할수 있게 해서
        # 현재 위치에대해 처음 dfs가 수행이 된것이기 때문에 그 위치에대해서 result값 증가 
        return True
        # 상하좌우에 대해서 호출된 내용들은 return 값을 사용하지 않기 때문에 단순히 연결된 
        # 모든노드들에 대해서 방문처리를 수행하기 위한 목적으로 수행됨 
        # 결과적으로 이 dfs는 한번 수행되면 해당노드와 연결된 모든 노드들도 방문처리 할수있도록하고
        # 시작점노드가 방문되었다면 즉 처음 방문하는 것이라면 그때만 result값을 증가시킴 
    # 현재 노드를 방문했다면 False반환
    return False
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(graph)
result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
