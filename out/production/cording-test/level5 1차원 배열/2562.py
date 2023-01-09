'''
문제
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

예를 들어, 서로 다른 9개의 자연수

3, 29, 38, 12, 57, 74, 40, 85, 61

이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

입력
첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

출력
첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.
'''

'''
A = []
max = 0
jarisu = 0
for i in range(9):
    B = int(input())
    A.append(B)

for i in range(9):
    if (A[i]>max):
        max = A[i]
        jarisu = i
print(max,jarisu+1)
파이썬은 리스트.index(max(리스트)) 이런식으로 max의 인덱스를
확인할수있음
'''

A = []
for i in range(9):
    A.append(int(input())) 
    # 이런식으로 입력하는걸 바로 리스트에 넣을수도있음
print(max(A))
#A의 최대값출력
print(A.index(max(A))+1)
#A의 최대값의 인덱스에 1을 추가해서 출력함 
#print(A.index(min(A))+1)