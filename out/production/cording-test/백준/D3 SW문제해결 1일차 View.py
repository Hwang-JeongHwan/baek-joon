#https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV134DPqAA8CFAYh&probBoxId=AV-HZfeqN3ADFASP&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part3&problemBoxCnt=14
# 691
# 9092
# 3 5 2 4 9 6 4 6
# 맨왼쪽 두칸과 맨 오른쪽 두카넹는 건물이 지어지 않음
tc = 10
for t in range(1, tc + 1):
    n = int(input())
    data = list(map(int, input().split()))
    count = 0
    for i in range(2, len(data) - 2):
        
        if data[i] - data[i - 1] > 0 and data[i] - data[i + 1] > 0 and data[i] - data[i - 2] > 0 and data[i] - data[i + 2] > 0:
            
            before1 = data[i] - data[i - 1]
            before2 = data[i] - data[i - 2]
            after1 = data[i] - data[i + 1]
            after2 = data[i] - data[i + 2]
            # if before1 == 0:
            #     before1 = int(1e9)
            # if before2 == 0:
            #     before2 = int(1e9)
            # if after1 == 0:
            #     after1 = int(1e9)
            # if after2 == 0:
            #     after2 = int(1e9)
            # print(before1, before2, after1, after2)
            count += min(before1, before2, after1, after2)

    print('#{} {}'.format(t, count))