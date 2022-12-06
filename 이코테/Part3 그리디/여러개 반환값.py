# 파이썬에서 함수는 여러 개의 반환 값을 가질 수 있음
def operator(a, b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var

a, b, c, d = operator(3, 7)
print(a, b, c, d)