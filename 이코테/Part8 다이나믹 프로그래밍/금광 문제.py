# 테스트 케이스 입력
t = int(input())
for i in range(t):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화 
    dp = []
    index = 0
    for i in range(n):
        # 0 ~ m까지 ->m ~ m+m 반복 n번
        # index~index+m 반복
        dp.append(array[index:index+m])
        index += m
    # 다이나믹 프로그래밍 진행
    # 0 1 1 1 2 1 3 1 
    # 열 기준으로 각 데이터를 확인하면서 테이블을 갱신
    # 매열을 하나씩 확인하며 즉 오른쪽으로 이동해 나가면서 각 열마다 전체 행을 확인 
    # 인덱스를 벗어나는지 확인하며 진행 
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0: left_up = 0
            else: left_up = dp[i - 1][j - 1]
            # 왼쪽 아래서 오는 경우
            if i == n - 1: left_down = 0 
            else: left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    
    result = 0
    for i in range(n):
        result = max(result,dp[i][m-1])
    print(result)
    
