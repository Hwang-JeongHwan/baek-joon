from collections import deque

n, k = map(int, input().split())
graph = []
test = []
for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(n):
        if graph[i][j] != 0:
            test.append((graph[i][j],0,i,j))

test.sort()


q = deque(test)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    virus, s, x, y = q.popleft()
    # print('q',virus,s,x,y)
    if s == target_s:
            break
    for j in range(4):    
        nx = x + dx[j]
        ny = y + dy[j]
        #    print('nx,ny',nx,ny)
        if nx >= 0 and ny >= 0 and nx < n and ny < n:
         #       print('check',virus)
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])