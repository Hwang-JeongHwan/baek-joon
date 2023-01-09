# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV19AcoKI9sCFAZN&probBoxId=AV-4MojKLNADFATz&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part4&problemBoxCnt=14

tc = int(input())

for t in range(1, tc + 1):
    s = input()
    data = [0] * len(s)
    count = 0
    for i in range(len(s)):
        if str(data[i]) != s[i]:
            count += 1
            for j in range(i, len(s)):
                data[j] = int(s[i])
    


    print('#{} {}'.format(t, count))