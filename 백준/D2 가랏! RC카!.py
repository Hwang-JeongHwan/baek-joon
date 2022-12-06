# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5PjMgaALgDFAUq&probBoxId=AV-HZfeqN3ADFASP&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part3&problemBoxCnt=14
tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    total = 0
    distance = 0
    for i in range(n):
        
        data = list(map(int, input().split()))
        if data[0] == 0:
            c = data
        else:    
            c = data[0]
            a = data[1]
        if c == 0:
            total = total
        
        if c == 1:
            total += a
        
        if c == 2:
            if total < a:
                total = 0
            else:
                total -= a
        distance += total
        
    print('#{} {}'.format(t, distance))