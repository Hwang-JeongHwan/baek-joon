'''
(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.



(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때
(3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

'''
A = int(input())
B = input()

AXB2 = A * int(B[2])
AXB1 = A * int(B[1])
AXB0 = A * int(B[0])
AXB = A * int(B)

print(AXB2,AXB1,AXB0,AXB, sep = '\n')
# sep='\n'로 줄바꿈
