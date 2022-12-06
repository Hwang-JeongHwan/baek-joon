# from re import A


# 두개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘으로는 유클리드 호제법이 있음

# 유클리드 호제법:
# 두자연수 A,B 에 대하여 (A > B) A를 B로 나눈 나머지를 R이라고 합시다
# 이때 A와 B의 최대공약수는 B와 R의 최대 공약수와 같음

# 유클리드 호제법의 아이디어를 그대로 재귀 함수로 작성할수 있음
# GCD(192, 162)
# A   B
# 192 162
# 162 30
# 30 12
# 12 6 => GCD(192, 162) = 6

def GCD(A, B):
    print(A, B)
    R = A % B
    if B % R == 0:
        return R
    return GCD(B, R)


print(GCD(162, 192))
def gcd(a, b):
    print(a, b)
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(162, 192))