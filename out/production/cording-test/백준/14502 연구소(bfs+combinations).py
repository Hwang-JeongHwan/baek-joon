import sys
import copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline
# 임의의 점 3개를 뽑고 bfs를 다 돌려봄, 제일 많은수가 나올때 return
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def count(copy_graph):
    result = 0
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j] == 0:
                result += 1
    return result


def bfs(check_point, graph, original_visited):
    queue = deque(check_point)
    copy_graph = copy.deepcopy(graph)
    visited = copy.deepcopy(original_visited)
    for i, j in queue:
        visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny] == 0:
                if copy_graph[nx][ny] == 0:
                    copy_graph[nx][ny] = 2
                    visited[nx][ny] = 1

                    queue.append((nx ,ny))

    return count(copy_graph)
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

original_visited = [[0] * m for _ in range(n)]
blank_point = []
virus_point = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus_point.append((i, j))
           
        if graph[i][j] == 0:
            blank_point.append((i, j))

result = 0
for a, b, c in combinations(blank_point, 3): # combinations(배열, 뽑을 원소 갯수)

    graph[a[0]][a[1]] = 1
    graph[b[0]][b[1]] = 1
    graph[c[0]][c[1]] = 1

    result = max(bfs(virus_point, graph, original_visited), result)
    
    graph[a[0]][a[1]] = 0
    graph[b[0]][b[1]] = 0
    graph[c[0]][c[1]] = 0

print(result)