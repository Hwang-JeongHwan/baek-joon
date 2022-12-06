for tc in range(1, 11):
    t = int(input())
    data = list(map(int, input().split()))
    while data[7] != 0:
        for i in range(1, 6):
            data[0] -= i

            data.append(data[0])
            data.pop(data.index(data[0]))
            if data[7] <= 0:
                data[7] = 0

                break

            #print(data)

    print('#{}'.format(t),end ='')
    for j in data:
        print(' {}'.format(j),end =' ')
