# 1,2 와 3,4가 팀이면
# S12+S21=1+4=5
# S34+S43=2+5=7

import sys
input = sys.stdin.readline
def dfs(idx, cnt):
    global result
    if cnt == N/2:
        start = 0
        link = 0
        for i in range(N):
            for j in range(N):
                if visited[i] == True and visited[j] == True:
                    start += l[i][j]
                elif visited[i] == False and visited [j] == False:
                    link += l[i][j]
        result = min(result,abs(start-link))
        return 
    #dfs로 팀원 분배
    for i in range(idx,N):
        if visited[i] == False:
            visited[i] = True
            dfs(i+1,cnt+1)
            visited[i] = False

N = int(input())
l = []
for i in range(N):
    l.append(list(map(int, input().split())))
result = 10000
visited = [False]*N
dfs(0,0)
print(result)