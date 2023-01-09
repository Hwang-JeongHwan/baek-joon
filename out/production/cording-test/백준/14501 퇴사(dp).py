n = int(input())
t_array = []
p_array = []
for _ in range(n):
    t, p = map(int, input().split())
    t_array.append(t)
    p_array.append(p)

dp = [0] * (n + 1)
# print(t_array, p_array)
max_value = 0
# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    t = i + t_array[i]
    
    
    # 상담 기간 안에 끝나는 경우
    if t <= n:
        
        # 현재까지의 최고 이익 계산
        dp[i] = max(p_array[i] + dp[t], max_value)
        max_value = dp[i]
    # 상담 기간을 벗어나는 경우
    else:
        dp[i] = max_value

print(max(dp))