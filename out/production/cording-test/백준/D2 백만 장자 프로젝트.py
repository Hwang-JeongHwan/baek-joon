# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5LrsUaDxcDFAXc&probBoxId=AV9gdM_anw0DFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part1&problemBoxCnt=20

tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    data = list(map(int, input().split()))
    # max_value = max(data)

    # count = 0
    # total = 0
    # result = 0
    # for i in range(n):
    #     if data[i] != max_value:
    #         total += data[i]
    #         count += 1
    #     else:
    #         result += (max_value * count) - total
    #         #print(result)
    #         if i + 1 < n:
    #             max_value = max(data[i + 1:]) 여기서 데이터가 겁나 많이들어오면
    #               시간이 오래걸려서 에러난듯?
            
    #             total = 0
    #             count = 0
            
    # print('#{} {}'.format(t, result))
    max_value = 0
    result = 0
    for i in range(n - 1, -1, -1):
        if max_value < data[i]:
            max_value = data[i]
        else:
            result += max_value - data[i]

    print('#{} {}'.format(t, result))
