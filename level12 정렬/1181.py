N = int(input())
l = []
for i in range(N):
    x = input()
    l.append(x)

s = set(l)

l1 = list(s)

l1.sort()
l1.sort(key = len)

for i in range(len(l1)):
    print(l1[i])