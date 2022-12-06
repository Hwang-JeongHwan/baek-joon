tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    result = [0] * 5

    while n > 1:
        if n % 2 == 0:
            n = n // 2
            result[0] += 1
        if n % 3 == 0:
            n = n // 3
            result[1] += 1
        if n % 5 == 0:
            n = n // 5
            # print(n)
            result[2] += 1
        if n % 7 == 0:
            n = n // 7
            result[3] += 1
        if n % 11 == 0:
            n = n // 11
            result[4] += 1
    

    print('#{}'.format(t), end=' ')
    for i in result:
        print(i, end=' ')
    print()