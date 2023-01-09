n = int(input())
for t in range(1, n + 1):
    s = input()
    data = [0] * len(s)
    count = 0
    
    
    for i in range(len(s)):
        if int(s[i]) != data[i]:
            count += 1
            for j in range(i, len(s)):
                data[j] = int(s[i])
            # print(data) 
           
    print('#{} {}'.format(t, count))