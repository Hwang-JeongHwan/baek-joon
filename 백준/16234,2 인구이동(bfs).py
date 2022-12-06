import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y): # count = 연합의 번호
    united = []
    united.append((x, y)) #연합이 된애들의 값을 바꿔줘야해서 배열을 새로만들고
    # 거기에 넣어줌 
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    total = graph[x][y]
    count_united = 1 # 연합 국가의 수 
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny] == 0:
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    visited[nx][ny] = 1
                    count_united += 1
                    total += graph[nx][ny]
                    queue.append((nx, ny))
                    united.append((nx, ny))
    total = total // count_united
    for x, y in united:
        graph[x][y] = total



n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


total_count = 0
while True:
    count = 0
    visited = [[0] * n for _ in range(n)] # 연합이 되면 그래프의 값이 바뀌니까
    # 연합이 만들어지고 그 다음날도 계속 진행하기 위해 이런식으로 계속 초기화 해주어야함
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs(i, j)
                count += 1
    if count == n * n: # 모든 인구이동이 끝나면 끝 
        break
    total_count += 1

print(total_count)
