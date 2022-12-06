# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5PmkDKAOMDFAUq&probBoxId=AV-HZfeqN3ADFASP&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%

tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    result = [0]
    for i in range(n):
        c, k = input().split()
        for j in range(int(k)):
            result.append(c)
    # print(len(result))
    print('#{}'.format(t))
    for i in range(1, len(result)):
        print(result[i], end ='')
        if i % 10 == 0:
            print()
    print()