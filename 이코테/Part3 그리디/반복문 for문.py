# 반복문으로 for문을 이용할 수도 있음
# for문의 구조는 다음과 같은데, 특정한 변수를 이용하여 'in'  뒤에 오는 데이터(리스트, 튜플 등)에 포함 되어있는
# 원소를 첫번째 인덱스부터 차례대로 하나씩 방문함

# for 변수 in 리스트:
#     실행할 소스코드 

array = [9, 8, 7, 6, 5]
for x in array:
    print(x)

# for문에서 연속적인 값을 차례대로 순회할 때는 range()함수를 주로 사용함
# 이때 range(시작 값, 끝 값 + 1)형태로 사용해야함
# 인자를 하나만 넣으면 자동으로 시작 값은 0이 됨

result = 0
# i는 1부터 9까지의 모든 값을 순회
for i in range(1, 10):
    result += i
print(result)

# 1부터 30까지의 모든 정수의 합 구하기
result = 0
for i in range(1, 31):
    result += i
print(result)