money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
tc = int(input())
for t in range(1, tc + 1):
    n = int(input())

    result = [0] * len(money)

    i = 0
    count = 0
    for i in range(len(money)):
        if n // money[i] > 0:
            count = n // money[i]
            result[i] = count
            n = n % money[i]

    print('#{}'.format(t))
    for i in result:
        print(i, end=' ')
    print()