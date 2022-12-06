def solution(x, y, count):


    if count == y:
        return x
    else:
        return x * solution(x, y, count + 1)


for i in range(10):
    t = int(input())
    x, y = map(int,input().split())
    count = 1
    print('#{} {}'.format(t, solution(x, y, count)))


