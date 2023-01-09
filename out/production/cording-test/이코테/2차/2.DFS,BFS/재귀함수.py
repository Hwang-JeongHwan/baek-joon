# 재귀함수(Recursive Fucntion)란 자기 자신을 다시 호출하는 함수를 의미함
# 단순한 형태의 재귀함수 예제
# 재귀 함수를 호출합니다. 라는 문자열을 무한히 출력함
# 어느정도 출력하다가 최대 재귀 깊이 초과 메시지가 출력됨

def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function() 