# 반복문을 즉시 탈출하고자 할 때 break를 사용함
# 1부터 5까지의 정수를 차례대로 출력하고자 할 때 다음과 같이 작성할수 있음

i = 1
while True:
    print('현재 i의 값:', i)
    if i == 5:
        break
    i += 1
    