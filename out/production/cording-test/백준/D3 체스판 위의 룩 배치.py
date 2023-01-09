tc = int(input())
for t in range(1, tc + 1):
    data = []
    for _ in range(8):
        data.append(list(input()))
    # print(data)
    flag = True
    count = 0
    for i in range(8):
        for j in range(8):
            if data[i][j] == 'O':
                count += 1
                #왼쪽
                for k in range(j):
                    if data[i][k] == 'O':
                        flag = False
                        break
                for k in range(j + 1, 8):
                    if data[i][k] == 'O':
                        flag = False
                        break

                for k in range(i):
                    if data[k][j] == 'O':
                        flag = False
                        break
                for k in range(i + 1, 8):
                    if data[k][j] == 'O':
                        flag = False
                        break

    if flag and count == 8:
        print('#{} {}'.format(t, 'yes'))
    else:
        print('#{} {}'.format(t, 'no'))