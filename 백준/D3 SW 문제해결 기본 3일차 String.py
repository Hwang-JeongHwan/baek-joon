tc = 10
for t in range(1, tc + 1):
    x = int(input())
    find = input()
    data = input()
    f_len = len(find)
    count = 0
    for i in range(len(data)):
        # print(i)
        s = data [i : f_len + i]
        # print(s)
        if s == find:
            count += 1
    print('#{} {}'.format(x, count))