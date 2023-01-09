from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

def bfs(x, y):
    start = graph[x][y]
    q = deque()
    q.append((x, y, start, 1))
    while q:
        x, y, start, count = q.popleft()
        time = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            time += 1
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] - 1 == graph[x][y]:
                time = 0
                q.append((nx, ny, start, count + 1))
        # if time == 4:
        #     result.append((start, count))
    result.append((start, count)) # 위코드랑 아래랑 같음 
tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    result = []
    for i in range(n):
        for j in range(n):
            bfs(i, j)
    result.sort(key = lambda x:(-x[1], x[0]))
    print('#{} {} {}'.format(t, result[0][0], result[0][1]))

# 2
# 2
# 1 2
# 3 4
# 3
# 9 3 4
# 6 1 5
# 7 8 2