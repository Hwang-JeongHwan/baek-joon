# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5PttaaAZIDFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part2&problemBoxCnt=14

tc = int(input())

for t in range(1, tc + 1):
    xh, xm, yh, ym = map(int, input().split())
    h = xh + yh
    m = xm + ym
    if m > 60:
        h += 1
        m -= 60
    

    if h > 12:
        h -= 12
    

    print('#{} {} {}'.format(t, h, m))