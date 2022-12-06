tc = int(input())
for t in range(1, tc + 1):
    n, m, k = map(int, input().split())

    data = list(map(int, input().split()))

    data.sort()
    # x초에 까지 만들어진 붕어빵의 개수는 (x // m) * k
    flag = True
    for i in range(n):
        total = ((data[i] // m ) * k ) - (i + 1) # 한개씩 사가므로 i + 1 만큼씩 빼주어야함
        # i = 0, data[i] = 2, m = 2, k = 1 , i + 1 = 1
        # total = 0, 0이어도 사갈수 있음
        if total < 0:
            flag = False
            break



    if flag:
        print('#{} {}'.format(t, 'Possible'))
    else:
        print('#{} {}'.format(t, 'Impossible'))

