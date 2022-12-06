for t in range(1, 11):
    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))

    count = 0 
    for i in range(n):
        stack = []
        for j in range(n):
            if data[j][i] == 1:
                stack.append(1)
            if data[j][i] == 2 and stack:
                stack.clear()
                count += 1
    
    print('#{} {}'.format(t, count))
