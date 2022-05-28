'''
문제
한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 x, y, w, h가 주어진다.

출력
첫째 줄에 문제의 정답을 출력한다.

제한
1 ≤ w, h ≤ 1,000
1 ≤ x ≤ w-1
1 ≤ y ≤ h-1
x, y, w, h는 정수
'''
'''
0,10           3,10
       26
                

0,0             3,0
'''
# import math
# w,h = 10,3

# a = [[0,0],[w,0],[0,h],[w,h]]

# print(a[0][0])
# x,y = 6,2

# # print(math.sqrt((x-a[0][0])**2+(y-a[0][1])**2))

# # print(math.sqrt(40))

# d = 1000
# for i in range(len(a)):
    
    
#     print(math.sqrt((x-a[i][0])**2+(y-a[i][1])**2))
#     if math.sqrt((x-a[i][0])**2+(y-a[i][1])**2) < d:
#         d = math.sqrt((x-a[i][0])**2+(y-a[i][1])**2)
            
# print(d)
        

x,y,w,h = map(int,input().split())
print(min(x,y,w-x,h-y))