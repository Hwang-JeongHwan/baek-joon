n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())
# print(data)
# print(add,sub,mul,div)
min_value = 1e9
max_value = -1e9

# 깊이 우선 탐색(DFS) 메서드

def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
        #print('add, sub, mul, div',add,sub,mul,div)
        
    else:
        if add > 0:
            add -= 1
            #print('add',i)
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            #print('sub',i)
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
           #print('mul',i)
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            #print('div',i)
            div -= 1
            dfs(i + 1, int(now / data[i]))
            div += 1




dfs(1,data[0])
print(max_value)
print(min_value)

