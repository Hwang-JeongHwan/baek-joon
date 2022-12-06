# 앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [0] * 100

# 보텀업 방식에서는 재귀함수가 아닌 반복문을 사용하기 때문에
# 시작 값을 배열에 저장해줌 -> 종료조건 대신에 점화식에서의 시작항의 값을 저장
# 1, 2번째 피보나치수는 1
d[1] = 1
d[2] = 1

n = 99
# 3번째부터 n번쨰 까지의 모든 피보나치수를 구하도록함

for i in range(3, n + 1):
    # 작은문제 부터 먼저 해결한 다음에 
    # 먼저 해결해 놓았던 그 작은 문제들을 조합해서 앞으로의 큰문제들을
    # 해결해 나갈수 있도록 함 
    d[i] = d[i - 1] + d[i - 2]

print(d[n])