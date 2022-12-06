for t in range(1, 11):
    n = int(input())
    data = []
    for i in range(8):
        data.append(list(input()))
    # print(data)
    count = 0
    for i in range(8):
        k = n
        
        for j in range(8 - n + 1):
            x = ''.join(data[i][j : j + k])
            # y = data[j: j + k][i]
            # print(x)
            if len(x) != 0 and x == x[::-1]:
                # print(x)
                count += 1

    for i in range(8):
        for j in range(8 - n + 1):
            y = ''
            for k in range(j, j + n):
                # print(k)
                y += data[k][i]
                if len(y) % n == 0 and y == y[::-1]:
                    count += 1



         


    print('#{} {}'.format(t, count))