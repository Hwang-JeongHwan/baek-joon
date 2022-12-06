# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV189xUaI8UCFAZN&probBoxId=AV-HZfeqN3ADFASP&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part3&problemBoxCnt=14

# A = 리터당 P원의 돈을 내야함
# B = 기본요금이 Q원이고 월간 사용량이 R리터 이하인 경우 요금은 기본 요금만 청구, 
# but R리터보다 많은 양을 사용한 경우 초과량에 대해 1리터당 S원의 요금을 더 내야함

tc = int(input())
for t in range(1, tc + 1):
    p, q, r, s, w = map(int, input().split())

    a = p * w
    b = 100
    if w <= r:
        b = q
    else:
        b = q + (w - r) * s
    
    if a < b:
        print('#{} {}'.format(t, a))
    else:
        print('#{} {}'.format(t, b))
        