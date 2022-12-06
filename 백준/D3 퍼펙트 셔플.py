tc = int(input())
for t in range(1, tc + 1):
    n = int(input())

    data = list(input().split())
    if n % 2 == 1:
        n_2 = (n // 2) + 1
    else:
        n_2 = n // 2
    up = data[:n_2]
    down = data[n_2:]
    # print(up, down)
    result = []
    for i in range(len(down)):
        result.append(up[i])
        result.append(down[i])
    if n % 2 == 1:
        result.append(up[-1])


    print('#{} {}'.format(t, ' '.join(result)))