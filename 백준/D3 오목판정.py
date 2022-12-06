dx = [-1, 1, 0, 0,-1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(input()))
    result = 'NO'
    flag = False
    for x in range(n):
        for y in range(n):

            if data[x][y] == 'o':

                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    count = 1
                    while True:
                        if nx < 0 or ny < 0 or nx >= n or ny >= n:
                            break
                        if data[nx][ny] == '.':
                            break

                        if data[nx][ny] == 'o':
                            count += 1
                        # print(count, nx, ny)
                        if count == 5:
                            flag = True
                            # print(x, y, nx, ny)
                            break
                        nx = nx + dx[i]
                        ny = ny + dy[i]


    if flag:
        print('#{} {}'.format(t, 'YES'))
    else:
        print('#{} {}'.format(t, 'NO'))