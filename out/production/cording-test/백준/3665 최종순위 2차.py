import sys
input = sys.stdin.readline
from collections import deque


def topology_sort():
    q = deque()
    result = []
    cycle = False
    only_one = True
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            only_one = False
            break
        now = q.popleft()
        result.append(now)
        for j in range(1, n + 1):
            if graph[now][j] == 1:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)
    
    if cycle:
        print('IMPOSSIBLE')
    elif only_one == False:
        print('?')
    else:
        for i in result:
            print(i, end=' ')
        print()

tc = int(input())
for t in range(tc):
    n = int(input())
    data = list(map(int, input().split()))
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for i in range(n):
        for j in range(i + 1, n):
            graph[data[i]][data[j]] = 1
            indegree[data[j]] += 1

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        # a <=> b 바꿔줘야함
        if graph[a][b] == 1:
            graph[b][a] = 1
            graph[a][b] = 0
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[b][a] = 0
            graph[a][b] = 1
            indegree[a] -=1
            indegree[b] += 1
    # topology_sort()


    q = deque()
    # 확실한 순위를 찾을수 없다면 '?' = > 진입차수가 0 인 노드가 여러개인 경우
    # 즉 답이 여러개인 경우
    # 순위를 정할 수 없는 경우에는 IMPOSSIBLE => 사이클이 발생한 경우
    result = []
    # 위상 정렬의 경우 n개가 큐에 들어갔다가 나옴 
    cycle = False
    only_one = True
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            only_one = False
            break
        now = q.popleft()
        result.append(now)
        for j in range(1, n + 1):
            if graph[now][j] == 1:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)
            
    if cycle:
        print('IMPOSSIBLE')
    elif only_one == False:
        print('?')
    else:
        for i in result:
            print(i, end = ' ')
        print()
    