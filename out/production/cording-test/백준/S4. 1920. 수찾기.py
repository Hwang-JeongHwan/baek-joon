import sys
input = sys.stdin.readline

n = int(input())
origin = set(map(int, input().split()))

flag = False
m = int(input())
data = list(map(int, input().split()))
for i in range(len(data)):
    if data[i] in origin:
        print(1)
    else:
        print(0)
    