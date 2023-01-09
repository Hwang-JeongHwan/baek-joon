'''
문제
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

입력
세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

출력
직사각형의 네 번째 점의 좌표를 출력한다.
'''

'''
    5,7          7,7     

    5,5          7,5

    10,20       30,20

    10,10       
'''

a = []
b = []
for i in range(3):
    x,y = map(int,input().split())
        
    a.append(x)
    b.append(y)

resultx = []
resulty = []
for i in range(3):
    
    if a.count(a[i]) <= 1:
        resultx.append(a[i])
    if b.count(b[i]) <=1:
        resulty.append(b[i])

print(resultx[0],resulty[0])

#print(min(a, key = a.count),min(b, key = b.count))
# sorted( , key = )처럼 안에 key값을 설정하여 원하는 방식으로 정렬조건을 조작할수있음
# 마찬가지로 min()도 안에 key값을 설정할수있음 
# 같은 x좌표가 몇개인지 key로 설정하여 min()으로 품 
#print(a.count)