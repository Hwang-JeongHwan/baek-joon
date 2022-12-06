tc = int(input())

for t in range(1, tc + 1):
    data = []
    for _ in range(9):
        data.append(list(map(int, input().split())))
    flag = True


    for i in range(9):
        row = []
        column = []
        for j in range(9):
            if data[i][j] in row:
                # print('i,j',i,j,row)
                flag = False
                break

            if data[i][j] not in row:
                row.append(data[i][j])
            if data[j][i] in column:
                flag = False
               # print('j,i',j,i, column)
                break

            if data[j][i] not in column:
                column.append(data[j][i])
    
    
    for i in range(0, 9, 3):
        index = 3
        for j in range(0, 9, 3):
            matrix = []
            for k in range(3):
                a, b, c = data[i + k][j : index]
                if a in matrix or b in matrix or c in matrix:
                    flag = False
                    break
                if a not in matrix and b not in matrix and c not in matrix:
                    matrix.append(a)
                    matrix.append(b)
                    matrix.append(c)
                
                #print(matrix)
            index += index
    if flag == True:
        print('#{} {}'.format(t, 1))
    else:
        print('#{} {}'.format(t, 0))



