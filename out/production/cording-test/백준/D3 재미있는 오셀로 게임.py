# 1이면 흑 2면 백
tc = int(input())

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]
row = [1, -1, 0 , 0]
column = [0, 0, 1, -1]



cross_x = [-1, -1, 1, 1]
cross_y = [-1, 1, -1, 1]
for t in range(1, tc + 1):
    n, m = map(int, input().split())

    graph = [[0] *(n + 1) for _ in range(n + 1)]
    n_2 = n // 2
    graph[n_2][n_2] = 2
    graph[n_2][n_2 + 1] = 1
    graph[n_2 + 1][n_2] = 1
    graph[n_2 + 1][n_2 + 1] = 2
    # print(graph)
    
    for _ in range(m):
        x, y, c = map(int, input().split())
        graph[x][y] = c
        # 가로 왼쪽으로 가는경우
        # 가로 오른쪽으로 가는경우
        # 세로 위로 가는경우
        # 세로 아래로 가는경우
        # 대각선 위로 가는경우 x, y 보다 작은경우 + x, y보다 큰경우
        # 대각선 아래로 가는경우  x, y 보다 작은경우 + x, y보다 큰경우


        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            count = 0
            while True:
                if nx < 1 or ny < 1 or nx >= n + 1 or ny >= n + 1:
                    break
                if graph[nx][ny] == 0:
                    break
                count += 1
                
                if graph[nx][ny] == c:
                    
                    rx = x
                    ry = y
                    # print('x',rx,ry,count)
                    # print('nx',nx, ny)
                    for j in range(count):
                        # print(j)

                        rx = rx + dx[i]
                        ry = ry + dy[i]
                        graph[rx][ry] = c


                    break
                nx = nx + dx[i]
                ny = ny + dy[i]
        
        # for i in range(8):
        #     nx = x + dx[i]
        #     ny = y + dy[i]
        #     data = []
        #     count = 0
        #     while True:
        #         if nx < 1 or ny < 1 or nx >= n + 1 or ny >= n + 1:
        #             data = []
        #             break
        #         if graph[nx][ny] == 0:
        #             data = []
        #             break
        #         if graph[nx][ny] == c:
                    
        #             break
        #         else:
        #             data.append((nx, ny))
        #         nx = nx + dx[i]
        #         ny = ny + dy[i]
            


        #     for i in range(len(data)):
        #         graph[data[i][0]][data[i][1]] = c
                
        # for i in range(4):
        #     nx = x + cross_x[i]
        #     ny = y + cross_y[i]
        #     count = 0
        #     while True:
        #         if nx < 0 or ny < 0 or nx >= n + 1 or ny >= n + 1:
        #             break
        #         count += 1
        #         if graph[nx][ny] == c:
                    
                    
        #             rx = x
        #             ry = y
        #             # print('cx',rx,ry,count)
        #             # print('cnx',nx, ny)
        #             for j in range(count):
        #                 # print(j)
        #                 # print('blrx',rx, ry)
                        
        #                 rx = rx + cross_x[i]
        #                 ry = ry + cross_y[i]
        #                 # print('alrx',rx, ry)
        #                 if c == 1:
        #                     if graph[rx][ry] == 2:
        #                         graph[rx][ry] = 1
        #                 if c == 2:
        #                     if graph[rx][ry] == 1:
        #                         graph[rx][ry] = 2
                                


        #             break
        #         nx = nx + cross_x[i]
        #         ny = ny + cross_y[i]

                
    count_1 = 0
    count_2 = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] == 1:
                count_1 += 1
            if graph[i][j] == 2:
                count_2 +=1
    
    print('#{} {} {}'.format(t, count_1, count_2))
    
# 1
# 4 12
# 1 2 1
# 1 1 2
# 4 3 1
# 4 4 2
# 2 1 1
# 4 2 2
# 3 4 1
# 1 3 2
# 2 4 1
# 1 4 2
# 4 1 2
# 3 1 2

