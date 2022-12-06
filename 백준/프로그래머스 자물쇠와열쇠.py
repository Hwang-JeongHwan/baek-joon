import sys

# 처음에 오른쪽을 보고 있으므로 동남서북으로

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'D':
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
    
    return direction


input = sys.stdin.readline
n = int(input())
k = int(input())

info = []
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1


l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

def simulate():
    x, y = 1, 1
    time = 0
    index = 0 # 다음에 회전할 정보
    graph[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 처음에는 동쪽을 보고 있음
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
            # 맵의 범위 안에 있고 뱀의 몸통이 없는 위치라면
        if nx > 0 and ny > 0 and nx <= n and ny <= n and graph[nx][ny] != 2:
            # 사과가 없다면 꼬리 제거
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                graph[px][py] = 0
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딫혔다면
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1

        if index < l and time == info[index][0]: # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())
            