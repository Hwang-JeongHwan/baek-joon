tc = 10


def solution():
    while True:
        j = 1
        for i in range(5):
            
            x = data.pop(0)
            # print(x)
            x -= j
            # print(x, j)
            if x <= 0:
                data.append(0)
                return
            data.append(x)
            j += 1
    



for t in range(1, tc + 1):
    n = int(input())
    data = list(map(int, input().split()))
    solution()
    print('#{} {}'.format(n, ' '.join(map(str, data))))
