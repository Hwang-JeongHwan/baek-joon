import sys
from itertools import combinations
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    for x, y in teacher:
        #print(x, y)
        
        if x >= 0:
            for j in range(x - 1, -1, -1):
         #       print('j',x, j)
                if graph[j][y] == 'S':
                    return False
                if graph[j][y] == 'O':
                    break
        if x < n:    
            for j in range(x + 1, n): # x + 1 부터 n - 1까지 반복
          #      print('j1',j)
                if graph[j][y] == 'S':
                    return False
                if graph[j][y] == 'O':
                    break

        if y >= 0:

            for j in range(y - 1, -1, -1): # y - 1 ~ 0 까지 -1 씩 감소하면서 진행
           #     print('j2',j)
                if graph[x][j] == 'S':
                    return False
                if graph[x][j] == 'O':
                    break
        if y < n:

            for j in range(y + 1, n):
            #    print('j3',j)
                if graph[x][j] == 'S':
                    return False
                if graph[x][j] == 'O':
                    break
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
