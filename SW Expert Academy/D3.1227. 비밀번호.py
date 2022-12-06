for tc in range(1, 11):
    t, data = input().split()
    data = list(data)

    i = 0
    while i < int(t):
        if i < (len(data) - 1):
            if data[i] == data[i + 1]:
                data.pop(i)
                data.pop(i)
                i = 0
            else:
                i += 1
        else:
            break
    result = ''.join(data)
    print('#{} {}'.format(tc, result))
