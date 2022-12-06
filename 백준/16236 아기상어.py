# 가장 처음 아기 상어의 크기 2
# 1초에 상하좌우로 인전한 한칸씩 이동
# 자기 자신보다 큰 물고기가 있는 ㅏㅋㄴ은 지날수 없고 나머지 칸은 모두 지날수
#있음 아기 상어는 자신의 크기보다 작은 물고기만 먹을수있음
# 크기가 같은 물고기는 먹을수 없지만 그 물고기가 있는 칸은 지나갈수있음

# 더이상 먹을수 있는 물고기가 공간에 없다면 엄마 상어에게 도움 요청
# 먹을수 있는 물고기가 1마리라면 먹으러감
# 먹을수 있는 물고기가 1마리보다 많으면
# 거리가 가장 가까운 물고기를 먹으러감
#
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def find_fish(ix, iy, shark):
    candidate = []
    q = deque()
    q.append((ix, iy, 0))
    visited = [[0] * n for _ in range(n)]
    while q:
        x, y, count = q.popleft()
        # 큐에서 꺼낸 좌표가 상어의 크기 보다 작고 => 먹을수 있는 물고기라면
        if graph[x][y] < shark and graph[x][y] != 0:
            # 후보 배열에 넣어줌 
            candidate.append((graph[x][y], x, y, count))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 현재 이동한 좌표가 상어의 크기 보다 작고 아직 방문하지 않은 곳이라면
            if graph[nx][ny] <= shark and visited[nx][ny] == 0:
                # 방문처리
                visited[nx][ny] = 1
                # 현재까지 이동한 거리만큼 큐에 넣어줌
                q.append((nx, ny, count + 1))
    # 거리가 가까운순, x좌표가 작은순, y좌표가 작은순으로 정렬후 return
    candidate.sort(key = lambda x: (x[3], x[1], x[2]))
    # print('cd', candidate)

    # 먹을수 있는 물고기가 없는경우
    if len(candidate) == 0:
        return 0
    else:
        # print(candidate[0][1], candidate[0][2])
        # 상어가 먹은 물고기가 있던곳의 좌표를 9로 바꿈 => 현재 상어 위치
        graph[candidate[0][1]][candidate[0][2]] = 9
        # 원래 상어의 위치를 0으로 바꿔줌
        graph[ix][iy] = 0
        # print(graph)
        # print('rt', candidate[0])
        return candidate[0]


def move_shark(x, y, shark):
    # 총거리
    count = 0
    # 먹은 물고기의 수
    fish_count = 0
    while True:
        # print(count)
        find = find_fish(x, y, shark)
        # print('f', find)

        # 먹을수 있는 물고기가 없는 경우 종료
        if find == 0:
            return count
        fish_count += 1
        # 먹은 물고기의 수가 상어의 크기와 같다면
        # 상어의 크기를 1 늘려줌
        if fish_count == shark:
            fish_count = 0
            shark += 1

        x = find[1]
        y = find[2]
        count += find[3]
        # print('nx',x, y, count)





n = int(input())
graph = []
shark = []
x = 0
y = 0
for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(n):
        if data[j] == 9:
            x = i
            y = j
            # graph[i][j] = 0
# find = find_fish(x, y, 2)
# print(find)
print(move_shark(x, y, 2))
