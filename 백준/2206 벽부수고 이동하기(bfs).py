import sys 
from collections import deque
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y, count):
    queue = deque()
    queue.append((x, y, count))
    visited[x][y][count] = 1

    while queue:
        x, y, count = queue.popleft()
        if x == n - 1 and y == m - 1: # 벽을 한번 부수고 최대가 되면
            # count = 0 일때는 x, y 가 n - 1, m -1 이 될수가 없음 
            # x == n - 1 and y == m - 1: 이렇게 됏다는거 자체가 최대값임
            # 벽을 한번도 부술 필요가 없으면 count = 1일때는 게속 0
            print(visited[x][y][count])
           
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny][count] == 0:
                if graph[nx][ny] == 0:
                    visited[nx][ny][count] = visited[x][y][count] + 1
                    queue.append((nx, ny, count))
                if graph[nx][ny] == 1 and count == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny ,1))
                
            # if count == 0 and graph[nx][ny] == 1 and visited[nx][ny][count] == 0: # 한번도 안부순경우 부서줌
            #     visited[nx][ny][1] = visited[x][y][count] + 1
            #     queue.append((nx, ny, 1))
            # if graph[nx][ny] == 0 and visited[nx][ny][count] == 0:
                
            #     visited[nx][ny][count] = visited[x][y][count] + 1
            #     queue.append((nx, ny, count))
            
            # if count == 0 and graph[nx][ny] == 1: # 한번도 안부순경우 부서줌
            #     visited[nx][ny][count + 1] = visited[x][y][count] + 1
            #     queue.append((nx, ny, count + 1))
            # if graph[nx][ny] == 0 and visited[nx][ny][count] == 0:
                
            #     visited[nx][ny][count] = visited[x][y][count] + 1
            #     queue.append((nx, ny, count))


n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))

for i in range(n):
    for j in range(m):
        graph[i][j] = int(graph[i][j])

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
# 3차원 리스트 만들어줌 입력받은 그래프에서 갚을 바로 바꾸면 안됨, 이러면 부순경우
# 안부순경우를 나눠서 거리를 구할수 없음 
# 벽을 부순경우 graph[x][y][z]에서 z = 1로
# print(visited)
bfs(0, 0, 0)
print(-1)


# if visited[n - 1][m - 1][0] == 0 and visited[n - 1][m - 1][1] == 0:
#     print(-1)
#     exit()
# else:
#     if visited[n - 1][m - 1][0] > visited[n - 1][m - 1][1]:
#         print(visited[n - 1][m - 1][0])
#         exit()
#     if visited[n - 1][m - 1][0] <= visited[n - 1][m - 1][1]:
#         print(visited[n - 1][m - 1][1])
#         exit()
#print(visited) 이렇게 출력하면 왜 안되는지는 모르겠음;;; 그냥 리턴 받아서 해야할듯

