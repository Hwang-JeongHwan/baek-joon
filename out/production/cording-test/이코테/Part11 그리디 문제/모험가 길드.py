n = int(input())
m = list(map(int, input().split()))

m.sort(reverse= True)
count = 0

# for i in range(n):
    
#     n = n % m[i]
#     i += m[i]
#     count += 1  
# print(count)  
y = n
x = 0
while x < y:
    # print(x)
    # print(m[x])
    n = n % m[x]
    x += m[x]
    count += 1
print(count)
# 문제를 잘못이해 -> 모든 모험가가 그룹에 포함되야 한다고 생각함....
