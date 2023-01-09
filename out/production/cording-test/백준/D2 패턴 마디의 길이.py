tc = int(input())
for t in range(1, tc + 1):
    data = input()
    flag = 0
    index = 0
    for i in range(1, 30 + 1):
        if data[index : i] == data[i : i + i]:
            flag = i
            break
    print('#{} {}'.format(t, flag))
    