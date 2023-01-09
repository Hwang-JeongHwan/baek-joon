tc = int(input())
for t in range(1, tc + 1):
    data = list(map(int, input().split()))
    result = round(sum(data) / 10)
    # round 두번째 인자 생략시 소수점 첫번째 자리에서 반올림됨
    # 파이썬에서의 round함수는 사사오입의 원칙을 따름
    # round(4.5) = 4
    # round(3.5) = 4 
    # 반올림 할때 앞자리가 짝수면 내리고 홀수면 올림
    
    print('#{} {}'.format(t, result))