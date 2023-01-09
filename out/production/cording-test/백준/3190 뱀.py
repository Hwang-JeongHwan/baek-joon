# 뱀은 처음에 오른쪽을 향함
# 몸 길이를 늘려 머리를 다음칸에 위치 시킴
# 만약 이동한 칸에 사과가 있다면 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않음
# 만약 이동한 칸에 사과가 없다면 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다
# 즉 몸 길이는 변하지 않는다

import sys
from collections import deque
# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]



def get_direction(c, direction):
    if c == 'D':
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
    return direction

def snake():
    x, y = 1, 1
    graph[x][y] = 2 #  머리가 있으면 2
    direction = 0
    t = 0
    index = 0
    q = deque()
    q.append((x, y))
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # print(direction)
        
        if nx > 0 and ny > 0 and nx <= n and ny <= n and graph[nx][ny] != 2:
            # 범위 내에 있고 사과가 있으면
            if graph[nx][ny] == 1:
                graph[nx][ny] = 2
                q.append((nx, ny))
            # 사과가 없으면 꼬리를 잘라줌
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.popleft()
                graph[px][py] = 0

        

        else:
            t += 1
            break
        x, y = nx, ny 
        t += 1
        # print(index, t)
        if index < l and info[index][0] == t:
            direction = get_direction(info[index][1], direction)
            # print('di',direction)
            index += 1


        
    return t



input = sys.stdin.readline
n = int(input())
k = int(input())

graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

info = []
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

print(snake())