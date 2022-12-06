import sys
from itertools import combinations
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    for x, y in teacher:
        if x >= 0: # 상
            nx = x
            while nx >= 0:
                if graph[nx][y] == 'S':
                    return False
                if graph[nx][y] == 'O':
                    break
                nx -= 1
        if x < n: #하
            nx = x
            while nx < n:
                if graph[nx][y] == 'S':
                    return False
                if graph[nx][y] == 'O':
                    break
                nx += 1
        if y >= 0: #좌
            ny = y
            while ny >= 0:
                if graph[x][ny] == 'S':
                    return False
                if graph[x][ny] == 'O':
                    break
                ny -= 1
        if y < n : # 우
            ny = y
            while ny < n:
                if graph[x][ny] == 'S':
                    return False
                if graph[x][ny] == 'O':
                    break
                ny += 1
    return True            
        
        


n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input().split()))
blank = []
teacher = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'X':
            blank.append((i, j))
        if graph[i][j] == 'T':
            teacher.append((i, j))
flag = 0
for a, b, c in combinations(blank, 3):
    graph[a[0]][a[1]] = 'O'
    graph[b[0]][b[1]] = 'O'
    graph[c[0]][c[1]] = 'O'
   # print(graph)
    if bfs():
        flag = 1
        print('YES')
        break
    graph[a[0]][a[1]] = 'X'
    graph[b[0]][b[1]] = 'X'
    graph[c[0]][c[1]] = 'X'
    

if flag == 0:
    print('NO')
