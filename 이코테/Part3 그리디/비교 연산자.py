# 비교 연산자는 특정한 두 값을 비교할 때 이용
# 대입 연산자(=) 와 같음 연산자(==)의 차이점에 유의

# X == Y : X와 Y 가 서로 같을대 참(True)이다
# X != Y : X와 Y가 서로 다를 때 참(True)이다.
# X > Y: X가 Y보다 클 때 참
# X < Y: X가 Y보다 작을 때 참
# X >= Y: X가 Y보다 크거나 같을 때 참
# X <= Y: X가 Y보다 작거나 같을 때 참

# 논리 연산자는 논리 값(True/False) 사이의 연산을 수행할 때 사용

# X and Y: X와 Y가 모두 참(True)일 떄 참(True)이다.
# X or Y: X와 Y 중에 하나만 참(True)이어도 참
# not X: X가 거짓(False)일 때 참

if True or False:
    print('yes')

if True and False:
    print('yess')

a = 15
if a <= 20 and a >= 0:
    print(a)