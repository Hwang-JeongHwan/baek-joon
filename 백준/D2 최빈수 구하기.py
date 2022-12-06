# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV13zo1KAAACFAYh&probBoxId=AV-HZfeqN3ADFASP&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part3&problemBoxCnt=14

# 최빈수 = 특정자료에서 가장 여러번 나타나는 값

# 10 8 7 2 2 4 8 8 8 9 5 5 3
# 이러면 8이 가장 많이 나와서 8이 최빈수임

tc = int(input())

for t in range(1, tc + 1):
    x = int(input())
    data = [0] * 101
    
    array = list(map(int, input().split()))
    for i in range(len(array)):
        data[array[i]] += 1
    max_value = max(data)
    result = []
    for i in range(len(data)):
        if data[i] == max_value:
            result.append(i)
    print('#{} {}'.format(t, max(result)))


