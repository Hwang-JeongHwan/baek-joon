import sys
N = int(sys.stdin.readline())

l = []
for i in range(N):
    a,b = map(int, sys.stdin.readline().split())
    l.append([a,b])

l.sort(key=lambda x:(x[1],x[0]))

for i in range(N):
    print(l[i][0],l[i][1])