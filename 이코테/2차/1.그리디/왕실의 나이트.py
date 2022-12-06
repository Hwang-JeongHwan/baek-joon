data = input()
array = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x = int(data[1])
y = data[0]
for i in range(9):
    if y == array[i]:
        y = i
#print(x, y)

dx = [-1, -1, 1, 1, -2, -2, 2, 2]
dy = [-2, 2, -2, 2, 1, -1, 1, -1]
count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    #print(nx, ny)
    if nx > 8 or ny > 8 or nx < 1 or ny < 1:
        continue
    count += 1
print(count)