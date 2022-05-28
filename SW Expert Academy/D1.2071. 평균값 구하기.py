t = int(input())

for i in range(1, t + 1):
    data = list(map(int,input().split()))
    result = sum(data) / len(data)
    print('#{} {}'.format(i, round(result)))