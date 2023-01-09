t = 10
for i in range(1, t + 1):
    dump = int(input())
    data = list(map(int, input().split()))
    for i in range(dump):
        x = data.index(max(data))
        y = data.index(min(data))
        data[x] -= 1
        data[y] += 1
    
    print('#{} {}'.format(max(data) - min(data)))

        