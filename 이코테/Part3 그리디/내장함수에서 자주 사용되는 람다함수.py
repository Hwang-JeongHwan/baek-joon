array = [('홍길동',50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1]


print(sorted(array, key = my_key))
print(sorted(array, key=lambda x: x[1]))