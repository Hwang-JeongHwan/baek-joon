for i in range(1,11):
    length = int(input())
    data = []
    count = 0
    for _ in range(8):
        data.append(list(input()))
    for j in range(8):
        x = ''
        y = ''
        for k in range(8):
            x += data[j][k]
            y += data[k][j]
        a = 0
        b = length
        while b < 9:
            x1 = x[a:b]
            y1 = y[a:b]
            # x2 = ''
            # y2 = ''
            # for l in range(length - 1,-1,-1):
            #     x2 += x1[l]
            #     y2 += y1[l]
            if x1 == x1[::-1]: # 문자열 뒤집는법 문자열[::-1]
                count += 1
            if y1 == y1[::-1]:
                count += 1

            a += 1
            b += 1
    print('#{} {}'.format(i, count))