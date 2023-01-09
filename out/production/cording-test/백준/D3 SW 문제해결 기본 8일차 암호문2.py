# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV14w-rKAHACFAYD&probBoxId=AV-4MojKLNADFATz&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part4&problemBoxCnt=14

# 0 ~ 999999

# l(삽입) x, y, s : 앞에서부터 x의 위치 바로 다음에 y개의 숫자를 삽입한다. s는 
# 덧붙일 숫자들이다

for t in range(1, 11):
    n = int(input())
    data = list(map(int, input().split()))
    op = int(input())  
    operation = list(input().split())
    
    for i in range(len(operation)):
        if operation[i] == 'I':
            for j in range(int(operation[i + 2])):
                # print(operation[i + j + 1], operation[i + j + 3])
                data.insert(int(operation[i + 1]) + j, int(operation[i + j + 3]))
                # print(data)
        if operation[i] == 'D':
            for j in range(int(operation[i + 2])):
                data.pop(int(operation[i + 1]))

    print('#{}'.format(t, end=' '))
    for i in range(10):
        print(data[i], end=' ')
    print()
