# 조건문에서 실행될 소스코드가 한 줄인 경우, 굳이 줄 바꿈을 하지 않고도 간략하게 표현할 수 있음

score = 85
if score >= 80: result = 'Success'
else: result = 'Fail'
print(result)

# 조건부 표현식(Conditional Expression)은 if ~ else 문을 한줄에 작성할수 있도록 해줌

score1 = 85
result1 = 'Success' if score1 >= 80 else 'Fail'
print(result1)
# 파이썬 조건문 내에서의 부등식
# 다른 프로그래밍 언어와 다르게 파이썬은 조건문 안에서 수학의 부등식을 그대로 사용할 수 있음
# 예를 들어 x > 0 and x < 20 과 0 < x <  20은 같은 결과를 반환함

x = 15
if x > 0 and x < 20:
    print('x는 0 이상 20 미만의 수입니다.')

x1 = 15
if 0 < x1 < 20:
    print('x1은 0 이상 20 미만의 수입니다.')

# but 본 책에서은 다른 언어를 다룰 때 헷갈리지 않도록 x > 0 and x < 20 와 같이 비교 연산자 사이에 and,
# or 등의 연산자가 들어가는 형태의 코드를 이용함
