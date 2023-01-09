# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5Pw_-KAdcDFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part2&problemBoxCnt=14

tc = int(input())
for t in range(1, tc + 1):
    data = list(map(int, input().split()))
    result = 0
    
    total = round((sum(data) - max(data) - min(data)) / 8)
    print('#{} {}'.format(t, total))