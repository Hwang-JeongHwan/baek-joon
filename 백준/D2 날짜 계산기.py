days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

tc = int(input())
for t in range(1, tc + 1):
    a_m, a_d, b_m, b_d = map(int, input().split())
    result = 0
    if a_m == b_m:
        result = b_d - a_d + 1

    if a_m < b_m:
        result = sum(days[a_m : b_m]) + (b_d - a_d) + 1
    print('#{} {}'.format(t, result))