'''
가장 왼쪽위 1,1
가장 오른쪽 아래 N,N

L R U D 중 하나의 문자가 반복적으로 적혀있음
L = 왼쪽으로 한칸
R = 오른쪽으로 한칸
U = 위로 한칸
D = 아래로 한칸

N X N 크기의 정사각형 공간을 벗어나는 움직임은 무시됨
(1,1)의 위치에서 L 혹은 U를 만나면 무시

LR은 x UD는 y축
'''
n = int(input())
x, y = 1,1
plans = input().split()

#L, R, U, D에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x+dx[i]
            ny = y+dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x,y = nx,ny

print(x,y)
