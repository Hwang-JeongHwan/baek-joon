tc = int(input())
for t in range(1, tc + 1):
    # L분 이상 U 분 이하의 운동, X분만큼 운동을 한 상황
    # 제한되어있는 시간을 넘은 운동을 한것인지 그것이 아니라면 몇분 더 운동을 해야
    # 제한을 맞출수있는지 출력하는 프로그램 작성
    l, u, x = map(int, input().split())
    if x < l:
        print('#{} {}'.format(t, l - x))

    if x >= l and x <= u:
        print('#{} {}'.format(t, 0))

    if x > u :
        print('#{} {}'.format(t, -1))