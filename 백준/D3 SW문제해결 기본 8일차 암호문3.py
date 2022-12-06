for t in range(1, 11):
    n = int(input())
    data = list(input().split())
    num = int(input())
    op = list(input().split())

    for i in range(len(op)):
        if op[i] == 'I':
            for j in range(int(op[i + 2])):
                data.insert(int(op[i + 1] ) + j, int(op[i + j + 3]))
        
        if op[i] == 'D':
            for j in range(int(op[i + 2])):
                data.pop(int(op[i + 1]))
        
        if op[i] == 'A': # 추가 암호문 맨뒤에 y개의 숫자를 덧붙인다
            for j in range(int(op[i + 1])):
                data.append(int(op[i + j + 2]))
    
    print('#{}'.format(t, end=' '))
    for i in range(10):
        print(data[i], end =' ')
    print()