# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV2b9AkKACkBBASw&probBoxId=AV-4MojKLNADFATz&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part4&problemBoxCnt=14

# R X C가 N이랑 최대한 가까우면 값이 최소화됨
tc = int(input())
for t in range(1, tc + 1):
    n, a, b = map(int, input().split())

    min_value = int(1e9)
    for r in range(1, n + 1):
        c = 1
        while r * c <= n:
            result = a * abs(r - c) + b * (n - r * c)
            # print(result)
            min_value = min(min_value, result)
            

            c += 1
    
    print('#{} {}'.format(t, min_value))