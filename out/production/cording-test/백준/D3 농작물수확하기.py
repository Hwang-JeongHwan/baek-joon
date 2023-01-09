tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(input()))

    start = n // 2
    end = n // 2 + 1
    total = 0
    i = 0
    while i < n:
        # print(i, start, end)
        total += sum(map(int, data[i][start:end]))
        if i < n // 2:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
        i += 1
    print('#{} {}'.format(t, total))