tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()
    print('#{}'.format(t),end=' ')
    for i in data:
        print('{}'.format(i), end =' ')
    print()