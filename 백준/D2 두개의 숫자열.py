tc = int(input())
for t in range(1, tc + 1):
    a, b = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    if a > b:
        a, b = b, a
        a_list, b_list = b_list, a_list
    # print(a, b)
    # print(a_list, b_list)
    result = 0
    for i in range(b - a + 1):
        total = 0
        for j in range(a):
            total += a_list[j] * b_list[i + j]
        # print(total)
        result = max(total, result)
    print('#{} {}'.format(t, result))
        