# 0 은 통로 1 은 벽 2 는 출발 3 은 도착
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, start):
    # global count

    q = deque()
    q.append((x, y, start))
    while q:
        x, y, count = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >=16 or ny >= 16 :
                continue

            if data[nx][ny] == '0':
                data[nx][ny] = '2'
                q.append((nx, ny, count + 1))
            if data[nx][ny] == '3':
                return True
    return False
tc = 10
for _ in range(1, tc + 1):
    t = int(input())
    data = []
    start = []
    for i in range(16):
        s = list(input())
        data.append(s)
        for j in range(len(s)):
            if s[j] == '2':

                start.append((i, j))

    x = start[0][0]
    y = start[0][1]

    # count = 0
    result = bfs(x, y, 0)
    # print(data)
    if result == False:
        print('#{} {}'.format(t, 0))
    else:
        print('#{} {}'.format(t, 1))
