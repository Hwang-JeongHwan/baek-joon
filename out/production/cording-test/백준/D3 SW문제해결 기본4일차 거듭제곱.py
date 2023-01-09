for _ in range(1, 11):
    t = int(input())
    n, m = map(int, input().split())
    print('#{} {}'.format(t, n ** m))
