tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(input()))

    mid = n // 2
    start = end = mid
    result = 0
    for i in range(n):
        for j in range(start, end + 1):
            result += int(data[i][j])
        
        if i < mid:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1

    print('#{} {}'.format(t, result))
    
