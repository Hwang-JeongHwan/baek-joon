n = int(input())

# n개의 원반을 시작에서 끝으로 이동
def hanoi(n, start, mid, end):
    if n == 1:
        print(start, end)
        return
    # 원판 n - 1을 중간으로 이동
    hanoi(n - 1, start, end, mid)
    # 가장큰 원반을 마지막으로 이동
    print(start, end)
    # 중간에있는 원반 n - 1개를 마지막으로 이동
    hanoi(n - 1, mid, start, end)

# 최소 횟수 = (2 ** n) - 1
print((2 ** n) - 1)
if n <= 20:
    hanoi(n, 1, 2, 3)