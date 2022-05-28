tc = 10

for i in range(tc):
    t = int(input())
    data = []
    for _ in range(100):
        data.append(list(map(int, input().split())))
    row = 0
    column = 0
    cross = 0
    max_row = 0
    max_column = 0
    max_cross = 0
    for j in range(100):
        for k in range(100):
            if j == k:
                cross += data[j][k]
            row += data[j][k]
            column += data[k][j]
        if max_row < row:
            max_row = row
        if max_column < column:
            max_column = column
        row = 0
        column = 0
    max_cross = cross
    cross = 0
    x = 99
    y = 0
    while x > -1:
        cross += data[x][y]
        # print(x,y)
        x -= 1
        y += 1
    if max_cross < cross:
        max_cross = cross
    # print(max_row,max_column,max_cross)
    print('#{} {}'.format(t, max(max_row, max_column, max_cross)))

