# 포탄 발사시 벽돌로 만들어진 벽 또는 강철로 만들어진 벽에 충돌하거나 
# 게입 맵 박으로 나갈때 까지 직진

# 포탄이 벽에 부딪히면 포탄은 소멸하고 부딪힌 벽이 벽돌로 만들어진
# 벽이라면 이 벽은 파괴되어 칸은 평지가 됨
# 강철로 만들어진 벽에 포탄이 부딪히면 아무일도 일어나지 않으ㅡㅁ
# 게임 맵밖으로 포탄이 나가면 아무일도 일어나지 안흥ㅁ

# . 평지 - 물
# * 벽돌
# # 강철
# S = 발사 

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

tc = int(input())
for t in range(1, tc + 1):
    h, w = map(int, input().split())
    data = []
    direction = 0

    x, y = 0, 0
    tank = ''
    for i in range(h):
        s = list(input())
        data.append(s)

        for j in range(len(s)):
            if s[j] == '^':
                direction = 0
                x = i
                y = j
                tank = '^'

            if s[j] == 'v':
                direction = 1
                x = i
                y = j
                tank = 'v'
            if s[j] == '<':
                direction = 2
                x = i
                y = j
                tank = '<'
            if s[j] == '>':
                tank = '>'
                direction = 3
                x = i
                y = j

    n = int(input())
    s = input()

    for i in range(n):
        # print(s[i])
        if s[i] == 'U':


            tank = '^'
            direction = 0
            data[x][y] = tank

            nx = x + dx[direction]
            ny = y + dy[direction]
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue

            if data[nx][ny] == '.':
                data[x][y] = '.'
                data[nx][ny] = tank
                x = nx
                y = ny

        if s[i] == 'D':

            tank = 'v'
            direction = 1
            data[x][y] = tank

            nx = x + dx[direction]
            ny = y + dy[direction]
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            
            if data[nx][ny] == '.':
                data[x][y] = '.'
                data[nx][ny] = tank
                x = nx
                y = ny

        if s[i] == 'L':

            tank = '<'
            data[x][y] = tank
            direction = 2
            nx = x + dx[direction]
            ny = y + dy[direction]
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            
            if data[nx][ny] == '.':
                data[x][y] = '.'
                data[nx][ny] = tank
                x = nx
                y = ny

        if s[i] == 'R':

            tank = '>'
            data[x][y] = tank
            direction = 3

            nx = x + dx[direction]
            ny = y + dy[direction]
            # print('R1',data)
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            
            if data[nx][ny] == '.':
                # print('R2',data)
            
                data[x][y] = '.'
                data[nx][ny] = tank
                # print('R3',data)
            
                x = nx
                y = ny

        if s[i] == 'S':

            # print(x, y, direction)
            nx = x + dx[direction]
            ny = y + dy[direction]
            # print(nx, ny)
            # print(data[nx][ny])
            while True:
                # print('in while',data[nx][ny], nx, ny)


                if nx < 0 or ny < 0 or nx >= h or ny >= w:

                    break
                if data[nx][ny] == '#' :
                    break
                if data[nx][ny] == '.' or data[nx][ny] == '-':
                    # print(nx, ny, direction)
                    nx = nx + dx[direction]
                    ny = ny + dy[direction]
                    continue

                if data[nx][ny] == '*':
                    data[nx][ny] = '.'
                    break
        # print(data)
    print('#{}'.format(t), end=' ')
    for i in range(h):
        for j in range(w):
            print(data[i][j],end='')
        print()
    