tc = int(input())

for t in range(1, tc + 1):
    data = list(map(int, input().split()))
    print('#{} {}'.format(t, max(data)))