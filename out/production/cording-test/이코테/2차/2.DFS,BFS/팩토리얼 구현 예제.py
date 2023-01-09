# n! = 1 x 2 x 3 x ''' x (n - 1) x n
# 수학적으로 0! 과 1!의 값은 1임

# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n 까지 수를 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    print(n)
    if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1

    # n! = n * (n - 1)! 를 그대로 코드로 작성하기
    return n * factorial_recursive(n - 1)
# 5 * factorial_recursive(4)
# 5 * 4 * factorial_recursive(3)
# 5 * 4 * 3 * factorial_recursive(2)
# 5 * 4 * 3 * 2 * factorial_recursive(1)
# 5 * 4 * 3 * 2 * 1


# 각각의 방식으로 구현한 n! 출력(n = 5)
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))