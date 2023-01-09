t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    data = []
    d = []
    x = m
    for i in range(n):
        data.append(array[i * m: x])
        x += m
    first = 0
    for i in range(n):
        if data[i][0] >= first:
            first = data[i][0]
            start = i
        
    d.append((first, start, 0))
    print(d)
    print(d)
    dx = [-1, 0, 1]
    
    for i in range(1, m):
        gold = 0
        start = 0
        for j in range(3):
            nx = d[i - 1][1] + dx[j]
            if nx < 0 or nx >= n:
                continue
            if data[nx][i] >= gold:
                gold = data[nx][i]
                start = nx
        d.append((gold + d[i - 1][0], start, i))
    print(d)
    print(d[m - 1][0])
   



    
        