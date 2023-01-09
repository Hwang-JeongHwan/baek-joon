t = 10
for i in range(10):
    n = int(input())
    data = list(map(int, input().split()))
    count = 0 
    for j in range(2, n - 2):
        l = []
        l.append(data[j - 1])
        l.append(data[j - 2])
        l.append(data[j + 1])
        l.append(data[j + 2])
        result = data[j] - max(l)
        if result < 0 :
            continue
        else:
            count += result
    print("#{} {}".format(i + 1, count))

        
    
    
    
