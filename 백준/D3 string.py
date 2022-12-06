tc = 10
for _ in range(1, tc + 1):
    t = int(input())
    find = input()
    s = input()

    j = len(find)
    count = 0
    for i in range(len(s)):

        if s[i : j] == find:
            count += 1
        j += 1

    print('#{} {}'.format(t, count))