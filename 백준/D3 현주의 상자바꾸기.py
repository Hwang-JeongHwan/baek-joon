# 상자는 처음에 모두 0


tc = int(input())
for t in range(1, tc + 1):
    n, q = map(int, input().split())
    box = [0] * (n + 1)
    for i in range(1, q + 1):
        l, r = map(int, input().split())
        for j in range(l, r + 1):
            box[j] = i
    print('#{}'.format(t), end=' ')
    for i in range(1, n + 1):
        print(box[i], end=' ')
    print()