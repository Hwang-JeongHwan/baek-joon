def solution_x(data):
    n = 100

    while True:
        for i in range(100):
            for j in range(100 - n + 1):
                x = ''.join(data[i][j: j + n])
                if x == x[:: -1]:
                    return len(x)
        n -= 1

        
            
def solution_y(data):
    n = 100
    while True:
        for i in range(100):
            for j in range(100 - n + 1):
                y = ''
                for k in range(j, j + n):
                    y += data[k][i]
                    if len(y) % n == 0:
                        if y == y[::-1]:
                            return len(y)
        
        n -= 1





for t in range(1, 11):
    n = int(input())
    data = []
    for _ in range(100):
        data.append(list(input()))

    x = solution_x(data)
    y = solution_y(data)
    result = max(x, y)
    print('#{} {}'.format(n, result))