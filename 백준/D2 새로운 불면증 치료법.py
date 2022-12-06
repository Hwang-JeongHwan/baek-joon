tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    x = n
    result = []
    
    while True:
        
        s = str(n)
        length = len(s)
        # print(s)
        for i in range(length):
            if s[i] not in result:
                result.append(s[i])
        
        
        if len(result) == 10:
            break
        n = n + x 
    
    print('#{} {}'.format(t, n))
