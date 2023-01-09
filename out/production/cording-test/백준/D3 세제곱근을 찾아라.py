tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    num = 1
    result = -1
    while True:
        temp = num * num * num

        if temp == n:
            result = num
            break
        elif temp > n:
            break
        num += 1

    print('#{} {}'.format(t, result))