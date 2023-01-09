from itertools import combinations

n = int(input())
board = [] # 복도 정보
teachers = [] # 선생님 좌표

spaces = [] # 빈 공간 좌표

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i,j))
        
        if board[i][j] == 'X':
            spaces.append((i,j))


def watch(x, y ,direction):
    # 위로 감시 
    if direction == 0:
        while x >= 0:
            if board[x][y] == 'S': # 학생인 경우
                return True 
            if board[x][y] == 'O': # 장애물인 경우
                return False
            x -= 1
    # 아래로 감시
    if direction == 1:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1

    # 왼쪽 방향으로 감시
    if direction == 2:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1
    
    # 오른쪽 방향으로 감시
    if direction == 3:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    return False

# 장애물 설치 이후에 한명이라도 학생이 감지되는지 검사
def process():
    # 모든 선생님의 위치를 확인
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                # 감지 되면 True
                return True
    # 안되면 False
    return False

find = False # 한명이라도 감지 되지 않도록 설치할 수 있는지 여부

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces,3):
    # 장애물 설치 해보기
    for x, y in data:
        board[x][y] = 'O'
        if process() == False:
            find = True
            break
    
    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')