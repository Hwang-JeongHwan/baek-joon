from collections import deque

tc = int(input())

# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def snail(n, t, graph):
    if n == 1:
        print('#{}'.format(t))
        print(1)
        return
    q = deque()
    q.append((0, 0, 0))
    graph[0][0] = 1
    visited[0][0] = True
    while q:
        direction, x, y = q.popleft()
        # print('x,y',x, y)
        nx = x + dx[direction % 4]
        ny = y + dy[direction % 4] 
        # print('nx,ny',nx, ny)
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            direction += 1
            nx = x + dx[direction % 4]
            ny = y + dy[direction % 4] 
            # print('a',nx, ny)
        if visited[nx][ny] == True:
            direction += 1
            nx = x + dx[direction % 4]
            ny = y + dy[direction % 4]

        if graph[nx][ny] == 0 and visited[nx][ny] == False:
            visited[nx][ny] = True
            graph[nx][ny] = graph[x][y] + 1
            q.append((direction, nx, ny))
    print('#{}'.format(t))
    for i in range(n):
        for j in range(n):
            print(graph[i][j], end=' ')
        print()
    


    
for t in range(1, tc + 1):
        
    n = int(input())
    visited = [[False] * n for _ in range(n)] 
    graph = [[0] * n for _ in range(n)]
    snail(n, t, graph)
    # print('#{}'.format(t))
    # for i in range(n):
    #     for j in range(n):
    #         print(graph[i][j], end=' ')
    #     print()
    