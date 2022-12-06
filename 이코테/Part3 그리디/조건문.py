# 조건문의 기본적인 형태 if ~ elif ~ else
# 조건문을 사용할 때 elif 혹은 else 부분은 경우에 따라서 사용하지 않아도됨

# if 조건문 1:
#     조건문 1 이 True  때 실행되는 코드

# elif 조건문 2:
#     조건문 1에 해당하지 않고, 조건문 2가 True일 때 실행되는 코드
# else:
#     위의 모든 조건문이 True 값이 아닐 때 실행되는 코드

a = -15
if a >= 0:
    print('a >=  0')
elif a >= -10:
    print('0 > a >= -10')
else:
    print('-10 > a' )

# 성적 구간에 따른 학점 출력 예제
score = 70
# 성적이 90점 이상일 때 : A
# 성적이 90점 미만, 80점 이상일 때: B
# 성적이 80점 미만, 70점 이상일 때: C
# 성적이 70점 미만일 때: F

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('F')