from collections import deque

n,m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    # 공백으로 구분되지않고 0과 1 로 구성된 문자열이 주어지기 때문에
    # 이와같이 단순히 문자열을 입력받은 다음에 각 원소에 대해서 인트형으로 바꾸어서
    # 다시 리스트로 만드는 방법을 사용 

# 이동할 네 방향 정의 (상, 하, 좌, 우)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y)) #튜플 자료형으로 넣어줌 
    # 큐가 빌 때까지 반복하기
    count = 0
    while queue:
        x, y = queue.popleft()
        # 반복할때마다 원소 하나를 꺼내서 현재 위치에서 4가지 방향으로의 위치 확인
        # 상, 하, 좌, 우 확인하기 위해 반복문을 4번 수행
        count += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로 찾기 공간을 벗어난 경우 무시 
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 벽인 경우 무시, 이문제에서는 0인경우임 
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문 하는 경우에만 최단 거리 기록
            # 그래프에서 1인경우 -> 지나갈수있는 경로임 
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
                # 다음으로 이동할 위치까지는 1만큼 거리가 먼것이기 떄문에 1을 더해서 넣어줌 

           
    # 가장 오른쪽 아래까지의 최단 거리 변환
   
    return graph[n-1][m-1]

print(bfs(0,0))
# graph의 [0][0]부터 시작 
