#


tc = int(input())
for t in range(1, tc + 1):
    k, n, m = map(int, input().split())
    data = [0] + list(map(int, input().split())) + [n]
    data.sort()
    start = 0
    count = 0
    for i in range(1, m + 2):
        if data[i] - data[i - 1] > k:
            count = 0
            break
        if data[i] - start > k:
            start = data[i - 1]
            count += 1



    if count != 0:
        print('#{} {}'.format(t, count))
    else:
        print('#{} {}'.format(t, 0))