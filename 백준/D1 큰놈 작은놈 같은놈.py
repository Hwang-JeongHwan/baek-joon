tc = int(input())
for t in range(1, tc + 1):
    a, b = map(int, input().split())
    if a > b:
        print('#{} >'.format(t))
    elif a < b:
        print('#{} <'.format(t))
    else:
        print('#{} ='.format(t))