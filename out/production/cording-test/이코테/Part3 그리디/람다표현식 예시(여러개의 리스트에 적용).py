list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)
# map함수 : 각각의 원소에 어떤 함수를 적용
# 첫번째 원소끼리 , 두번쨰 원소끼리 이런식으로 순서에 맞는 원소끼리 더한결과를 별도의 리스트에 담고자 할수있음
# 이럴때 이러한 코드가 사용될수있음 

print(list(result))

print(list1 + list2)