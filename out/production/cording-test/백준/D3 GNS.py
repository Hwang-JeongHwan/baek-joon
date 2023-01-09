num = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7,
       "EGT":8, "NIN":9}

alpha = {0:"ZRO", 1:"ONE", 2:"TWO", 3:"THR", 4:"FOR", 5:"FIV", 6:"SIX",
         7:"SVN", 8:"EGT", 9:"NIN"}


tc = int(input())
for _ in range(1, tc + 1):
    t, n = input().split()
    s = input().split()
    n = int(n)
    data = []
    for i in range(n):
        if s[i] in num:
            data.append(num[s[i]])

    data.sort()
    for i in range(n):
        if data[i] in alpha:
            data[i] = alpha[data[i]]
    print('{}'.format(t))
    print(' '.join(data))