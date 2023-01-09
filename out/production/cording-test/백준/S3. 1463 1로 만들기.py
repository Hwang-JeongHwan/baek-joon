# x가 3으로 나누어 떨어지면 3으로 나눔
# X가 2로 나누어 떨어지면 2로 나눔
# 1을 뺸다
import sys
input = sys.stdin.readline

x = int(input())
dp = [0] * (x + 1)
for i in range(2, x + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[x])