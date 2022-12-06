# x % 5 == 0  => x//5
# x % 3 == 0 => x//3
# x % 2 ==0 => x//2
# x - 1

# x - 1 을 했을때와 안했을떄

x = int(input())
d = [0] * 30001
for i in range(2, x + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = max(d[i], d[i // 2] + 1)
    
    if i % 3 == 0:
        d[i] = max(d[i], d[i // 3] + 1)
    
    if i % 5 == 0:
        d[i] = max(d[i], d[i // 5] + 1)
print(d[x])