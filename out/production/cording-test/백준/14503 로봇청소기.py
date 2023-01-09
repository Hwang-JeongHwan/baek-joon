# https://www.acmicpc.net/problem/14503
from collections import deque

rx = [-1, 0, 1, 0]
ry = [0, 1, 0, -1]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def simulate(x, y, count, direction):
    time = 0
    visited[x][y] = 1
    count += 1
    while True:
        direction -= 1

        nx = x + dx[direction % 4]
        ny = y + dy[direction % 4]
        if visited[nx][ny] == 0 and data[nx][ny] == 0:
            visited[nx][ny] = 1 # 방문처리
            time = 0 # 돈 횟수 초기화
            count += 1 # 청소 횟수 + 1
            x = nx # 위치 이동
            y = ny
            continue
        else:
            time += 1

        if time == 4:
            nx = x - dx[direction % 4]
            ny = y - dy[direction % 4]
            if data[nx][ny] == 0:
                x = nx
                y = ny
                time = 0

            else:
                return count



n, m = map(int, input().split())
r, c, direction = map(int, input().split())
data = []
visited = [[0] * m for _ in range(n)]
for _ in range(n):
    data.append(list(map(int, input().split())))

print(simulate(r, c, 0, direction))
