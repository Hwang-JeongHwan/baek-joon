tc = 10
for _ in range(tc):
    t = int(input())
    search = input()
    data = input()
    count = 0
    s = ''
    for i in data:
        s += i
        if search in s:
            count += 1
            s = ''


    print('#{} {}'.format(t, count))