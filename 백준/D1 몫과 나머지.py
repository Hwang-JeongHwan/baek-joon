tc = int(input())
for t in range(1, tc + 1):
    a, b = map(int, input().split())
    print('#{} {} {}'.format(t, a // b, a % b))