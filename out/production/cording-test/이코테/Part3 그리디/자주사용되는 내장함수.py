# sum() 리스트나 튜플의 합
result = sum([1, 2, 3, 4, 5])
print(result)

# min(), max() 인자로 여러개의 값을 넣어줄수있고 이중에서 가장 작은값 혹은 큰값을 반환함 
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
print(min_result, max_result)

# eval() 흔히 사람의 입장에서 수식으로 표현된 하나의 식이있을때 실제 수 형태로 반환해주는 함수
result = eval('(3+5)*7')
print(result)

# sorted() 리스트와 같은 반복가능한 객체가 들어왔을때 정렬가능 reverse=True시 내림차순으로 정렬 
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4],reverse=True)
print(result)
print(reverse_result)

# sorted() with key => key속성으로 정렬기준을 명시해줄 수 있음 
array = [('홍길동', 25, 121), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)