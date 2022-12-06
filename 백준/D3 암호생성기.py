
tc = 10
for _ in range(1, tc + 1):
    t = int(input())
    data = list(map(int, input().split()))
    while True:
        for i in range(1, 6):
            now = data.pop(0)
            now -= i
            if now <= 0:
                now = 0
                data.append(now)
                break
            else:
                data.append(now)

        if data[-1] == 0:
            break

    print('#{}'.format(t), end=' ')
    print(*data)
    
    