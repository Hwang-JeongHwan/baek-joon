# 0부터 9까지의 수를 포함하는 리스트
array = [i for i in range(10)] # 대괄호 안에 반복문 사용
#  i라는 값이 0부터 9까지 매번 증가를 하면서 반복을 할때마다 그 i 의 값들을 원소로 설정해서

# 리스트를 만듬
# 다시 말해서 range함수를 단순히 10이라고 쓰게되면 0부터 9까지 값을 i가 순회하도록함
print(array)

array1 = [i for i in range(20) if i % 2 == 1] #홀수만 포함하는 리스트
print(array1)

array2 = [i * i for i in range(1, 10)]
print(array2)

# N X M 크기의 2차원 리스트를 한번에 초기화
n = 2
m = 3

array3 = [[0] * m for _ in range(n)]
# n번 반복할 때마다 길이가 m인 리스트를 새롭게 초기화 하는 방식으로 전체 리스트를 구성
print(array3)

# 변수명.count(특정값) 리스트에서 특정한 값을 가지는 데이터의 개수를 셀 때 사용한다

