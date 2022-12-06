# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV5PwGK6AcIDFAUq&probBoxId=AV9oaSMa3DEDFAQc&type=PROBLEM&problemBoxTitle=%5BD1%7ED2+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part2&problemBoxCnt=14
# A+ A0 A- B+ B0 B- C+ C0 C- D0
# 총점 = 중간고사 35% 기말고사 45% 과제 20%


# 각각의 평점은 같은 비율로 부여할수 있고
# N명의 학생이 있을 경우 N/10명의 학생들에게 동일한 평점을 부여할 수 있음

score = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']
score.reverse()
#print(score)
tc = int(input())
for t in range(1, tc + 1):
    n, k = map(int, input().split())
    data = []
    for i in range(1, n + 1):
        a, b, c = map(int, input().split())
        total = (a * 0.35) + (b * 0.45) + (c * 0.20)
        data.append((total, i))

    # print(data)
    data.sort(reverse=True)
    # print(data)
    for i in range(n):
        if data[i][1] == k:
            # 100명중 2등이면 score[0] 20 등이면 score[2]를 출력해야 하므로
            # n // 10 으로 i를 나눠줘야함
            # i // (n // 10) 
            # 위의 식에서 i = 2 : 2 // (100 // 10) =>  0 이 나옴
            # i = 20 : 20 // (100 // 10 ) = > 2이 나옴
            
            print('#{} {}'.format(t, score[i // (n // 10)]))
        