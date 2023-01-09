t = int(input())
for _ in range(t):
    array = [0] * 101
    result = []
    a = int(input())
    data = list(map(int ,input().split()))
    for i in data:
        array[i] += 1

    for j in range(len(array)):
        if array[j] == max(array):
            result.append(j)

    print('#{} {}'.format(a,result[-1]))

