# 금광의 모든 위치에 대하여 다음의 세가지만 고려하면됨
# 1. 왼쪽 위에서 오는 경우
# 2. 왼쪽 아래에서 오는경우
# 3. 왼쪽에서 오는 경우
# 세가지 경우에서 가장 많은 금을 가지고 있는 경우를 테이블에 갱신해주어 문제를 해결

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    index = 0
    dp = []
    for i in range(n):
        dp.append(array[index : index + m])
        index += m
    
    print(dp)
    # 열기준으로 매 열을 확인
    
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는경우
            if i == 0: 
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]

            left = dp[i][j - 1]
            print(i,j, left_up, left, left_down)
            print(max(left_up, left, left_down))
            dp[i][j] = dp[i][j] + max(left_up, left, left_down)
    
    result = 0
    print(dp)
    for i in range(n):
        for j in range(m):
            if dp[i][j] >= result:
                result = dp[i][j]
    print(result)

