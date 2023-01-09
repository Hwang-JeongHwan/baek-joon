tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    data = []
    for i in range(n):
        a, b = map(int, input().split())
        data.append((a, b))
    bus = []
    p = int(input())
    for i in range(p):
        bus.append(int(input()))

    result = [0] * p
    # print(data)
    # print(bus)
    for i in range(n):
        for j in range(p):
            if data[i][0] <= bus[j] and data[i][1] >= bus[j]:
                result[j] += 1

    print('#{} '.format(t), end='')
    for i in result:
        print(i, end=' ')
    print()