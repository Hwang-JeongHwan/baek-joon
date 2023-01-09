

tc = int(input())
for t in range(1, tc + 1):
    dic = {'S': 13, 'D': 13, 'H': 13, 'C': 13}
    card = []
    flag = True
    s = input()
    for i in range(0, len(s), 3):

        if (s[i], int(s[i + 1 : i + 3])) not in card:
            card.append((s[i], int(s[i + 1 : i + 3])))
            dic[s[i]] -= 1
        else:
            flag = False
            break

    if flag:
        print('#{}'.format(t),end=' ')
        for value in dic.values():
            print(value, end=' ')
        print()
    else:
        print('#{} ERROR'.format(t))