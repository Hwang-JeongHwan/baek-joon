import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    data = list(map(int, input().split()))
    # 각 노드에 연결된 간선 정보를 담기 위한 인접 행렬 초기화
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    # 방향 그래프의 간선의 정보 초기화
    for i in range(n):
        for j in range(i + 1, n):
            # i = 0, j = 1, 2, 3, 4
            # data[i] = 5 
            # data[j] = 4 3 2 1
            graph[data[i]][data[j]] = 1
            indegree[data[j]] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if graph[a][b] == 1:
            graph[a][b] = 0
            graph[b][a] = 1
            indegree[a] += 1 
            indegree[b] -= 1
        else:
            graph[a][b] = 1
            graph[b][a] = 0
            indegree[a] -= 1
            indegree[b] += 1

    # 일반적인 위상정렬의 경우 정확히 N개의 노드가 큐에서 출력된다.
    # 노드가 n번 나오기 전에 큐가 비게된다면 사이클이 발생한것
    # 특정 시점에서 2개 이상의 노드가 큐에 한꺼번에 들어갈 때는 가능한 정렬결과가
    # 여러가지라는 의미임
    # 그러므로 위상정렬 수행 과정에서 큐에서 노드를 뽑을 때 큐의 원소가 항상 1개로
    # 유지되는 경우에만 고유한 순위가 존재하는 것으로 이해할 수 있다.
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    cycle = False
    only_one = True
    result = []
    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            only_one = False
            break
        now = q.popleft()
        result.append(now)
        for i in range(1, n + 1):
            if graph[now][i] == 1:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
    
    if cycle:
        print('IMPOSSIBLE')
    elif only_one == False:
        print('?')
    else:
        for i in range(n):
            print(result[i], end=' ')
        print()

