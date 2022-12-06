n = int(input())
data = input().split()
x, y = 1, 1
# L R U D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0 ,0]

for i in data:
    if i == 'L':
        nx = x + dx[0]
        ny = y + dy[0]
        if nx >= 1 and ny >= 1 and nx <= 5 and ny <= 5:
            x = nx
            y = ny
    if i == 'R':
        nx = x + dx[1]
        ny = y + dy[1]
        if nx >= 1 and ny >= 1 and nx <= 5 and ny <= 5:
            x = nx
            y = ny
    
    if i == 'U':
        nx = x + dx[2]
        ny = y + dy[2]
        if nx >= 1 and ny >= 1 and nx <= 5 and ny <= 5:
            x = nx
            y = ny
    
    if i == 'D':
        nx = x + dx[3]
        ny = y + dy[3]
        if nx >= 1 and ny >= 1 and nx <= 5 and ny <= 5:
            x = nx
            y = ny

print(x, y)
            
