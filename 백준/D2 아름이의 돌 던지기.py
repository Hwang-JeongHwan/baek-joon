# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV18-stqI8oCFAZN&probBoxId=AV-HZfeqN3ADFASP&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part3&problemBoxCnt=14

# -100000 ~ 100000

tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    data = list(map(int, input().split()))
    result = []
    for i in range(n):
        result.append(abs(0 - data[i]))
    # print(result)
    min_value = min(result)
    # print(result.count(min_value))
    print('#{} {} {}'.format(t, min_value, result.count(min_value)))