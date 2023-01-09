import sys
input = sys.stdin.readline

def binary_search(data, start, end):
    result = 0
    while start <= end:
        first = data[0] # 맨처음꺼는 설치한다고 가정
        mid = (start + end) // 2
        count = 1
        for i in data:
            if i >= mid + first:
                first = i
                count += 1
        if count >= c:
            start = mid + 1
            result = mid
        else: 
            end = mid - 1
    return result


n, c = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort()
start = 1 # 최소거리
end = data[-1] - data[0] # 최대거리
print(binary_search(data, start, end))