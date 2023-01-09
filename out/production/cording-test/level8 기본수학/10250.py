'''
C-A = 층 만약 10보다 작으면 *10 해줌 
C-A를 반복한횟수 = 방번호 
C-A가 0보다는 클때까지 반복
C-A>0이면 해당 층 1호 주면됨 
'''

N = int(input())
for i in range(N):
    A,B,C = map(int,input().split())
    count = 1
    while True :
        if (C-A) > 0 :
            C -= A
            count+=1
        else:
            
            if C<0:
                C+=A
            
            if count<10:
                x=(C)*10
                print(str(x)+str(count))
                break
            else:
                x=C
                print(str(x)+str(count))
                break

