# push x: 정수 x를 스택에 넣는 연산
# pop : 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다
# 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다 만약 스택에 들어있는 정수가 없는 경우에는
# -1 을 출력한다.
import sys
input = sys.stdin.readline
n = int(input())
result = []
for i in range(n):
    data = list(input().rstrip().split())
    if len(data) > 1:
        result.append(int(data[1]))
    
    if data[0] == 'top':
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])
    
    if data[0] == 'pop':
        if len(result) == 0:
            print(-1)
        else:
            print(result.pop())
    
    if data[0] == 'empty':
        if len(result) == 0:
            print(1)
        else:
            print(0)
    if data[0] == 'size':
        print(len(result))