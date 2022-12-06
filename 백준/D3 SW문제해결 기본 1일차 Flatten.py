tc = 10
for t in range(1, tc + 1):
    n = int(input())
    data = list(map(int, input().split()))
    # print(len(data))
    for i in range(n):
        max_index = data.index(max(data))
        min_index = data.index(min(data))
        data[max_index] -= 1
        data[min_index] += 1

    print('#{} {}'.format(t, max(data) - min(data)))


