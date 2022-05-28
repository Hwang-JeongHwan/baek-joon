n,m = map(int, input().split())
a = []
for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)
# print(a)
# b = min(a[0])   
# print(b) 
b = 0
for i in range(n):
    if b < min(a[i]):
        b = min(a[i])
print(b)