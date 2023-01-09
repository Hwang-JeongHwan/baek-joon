# 정렬하고 가운데 값을 print하면됨
# 가장 작은 값을 출력하므로 data.sort() -> print(data[(n - 1 // 2)])
# 가장 큰값이었으면 반올림 하거나 + 1 해주면 됨 
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

# result = 1e9
# min_result = 0
# for i in range(1, max(data) + 1):
#     total = 0
#     for j in range(n):
#         total += abs(data[j] - i)
#     if result > total:
#         result = total
#         min_result = i

# print(min_result)
data.sort()
start = 0
end = n - 1
mid = (start + end) // 2
#print(data[mid])
print(data[(n - 1) // 2])