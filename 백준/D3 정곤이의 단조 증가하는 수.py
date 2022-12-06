# 단조 증가인지 체크하는 함수
def check(number):
    s = str(number)
    for i in range(1, len(s)):
        if s[i - 1] > s[i]:
            return False
    return True


tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    data = list(map(int, input().split()))

    result = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            mul = data[i] * data[j]
            if check(mul):
                result = max(mul, result)
    if result == 0:
        result = -1
        
    print('#{} {}'.format(t, result))
