from collections import deque
import sys

input = sys.stdin.readline
#f는 총 층수
# s = 현재 층
# g = 이동하려고 하는 층
# u = u층 위로 가는 버튼
# d = g층 아래로 가는 버튼

f, s, g, u, d = map(int, input().split())

dx = [u, -d]
visited = [0] * (f + 1)

def bfs(s, count):
    q = deque()
    q.append((s, count))
    visited[s] = count + 1

    while q:
        x, count = q.popleft()
        for i in range(2):
            nx = x + dx[i]
            # print('f',nx)
            if nx > 0 and nx <= f and visited[nx] == 0:
                visited[nx] = count + 1
                q.append((nx, count + 1))
                # print('n', nx)

bfs(s, 0)
# print(visited)
if s == g:
    print(0)
else:
    if visited[g] != 0:
        print(visited[g])
    else:
        print('use the stairs')


