'''
문제설명
당신은 화성 탐사 기계를 개발하는 프로그래머이다. 그런데 화성은 에너지 공급원을 찾기가 힘들다. 그래서 에너지를 효율적으로 사용하고자 화성 탐사 기계가 출발 지점에서 목표 지점까지 이동할 때 항상 최적의 경로를 찾도록 개발해야 한다. 화성 탐사 기계가 존재하는 공간은 N X N 크기의 2차원 공간이며, 각각의 칸 을 지나기 위한 비용(에너지 소모량)이 존재합니다. 가장 왼쪽 위 칸인 [0][0] 위치에서 가장 오른쪽 아래 칸인 [N-1][N-1] 위치로 이동하는 최소 비용을 출력하는 프로그램을 작성해라. 화성 탐사 기계는 특정한 위치에서 상하좌우 인접한 곳으로 1칸씩 이동할 수 있다.

입력조건
첫째 줄에 테스트 케이스의 수 T(1 <= T <= 10)가 주어진다.
매 테스트 케이스의 첫째 줄에는 탐사 공간의 크기를 의미하는 정수 N이 주어진다.(2 <= N <= 125) 이어서 N개의 줄에 걸쳐 각 칸의 비용이 주어지며 공백으로 구분한다.(0 <= 각 칸의 비용 <= 9)
출력조건
각 테스트 케이스마다 [0][0]의 위치에서 [N-1][N-1]의 위치로 이동하는 최소 비용을 한 줄에 하나씩 출력한다.
'''                    
# 시작 위치에서 마지막 위치까지의 최소 비용 계산
# 다익스트라 사용 하면 될듯
# 2 <= N <= 125라 플로이드도 가능할듯

import sys
import heapq
def dijkstra(x, y):
    q = []
    heapq.heappush(q,(0, x, y))
    distance[x][y] = 0

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                # print(nx, ny, distance[nx][ny])  
                distance[nx][ny] = cost
                # print(nx, ny, distance[nx][ny])  
                
                heapq.heappush(q, (distance[nx][ny], nx, ny))

            


input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    graph = []
    INF = int(1e9)
    distance = [[INF] * n for _ in range(n)]
    for i in range(n):
        graph.append(list(map(int, input().split())))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dijkstra(0, 0)

    print(graph[0][0] + distance[n - 1][n - 1])
