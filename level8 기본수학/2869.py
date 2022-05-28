'''
문제
땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)

출력
첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.
'''
'''
A,B,V = map(int,input().split())

total = 0
count = 0
while True:
    total+=A #올라가는건 하루가 더 지나야 올라감
    count+=1 #카운트를 늘려주고
    if(total<V): #아직 작다면
        total-=B #내려간뒤 다음날로감 
        
        
    else :
        break #같거나 total이더 크면 멈춤 

        

print(count)

시간초과 걸림;;

'''
A,B,V = map(int,input().split())

height = V-A # 2 1 5라면 height = 3
if height % (A-B) == 0: # height % (A-B) == 0
    first = int(height/(A-B)) # 3/1 = 3 + 1 

else:
    first = int(height/(A-B)+1)
print(first+1)