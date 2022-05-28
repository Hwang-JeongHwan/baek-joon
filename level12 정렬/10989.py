import sys

N = int(input())

counting_list = [0]*10001



for i in range(N):
    x = int(sys.stdin.readline())
    counting_list[x] += 1 #리스트의 x번째 수를 +1 시켜줌 초기값은 다 0임 

for i in range(1,10001): # 1<i<10001까지의 수
    if counting_list[i]>0: # counting_list의 i번쨰 수가 0보다크면
        # 즉 한개 이상 존재하면
        #print('counting_list[i]',counting_list[i])
        for j in range(counting_list[i]):# counting_list[i]만큼 반복
            # 2이면 2번 3이면 3번 1이면 1번
            print(i) # i를출력 -> i가 list의 인덱스이고 인덱스별로 카운팅 햇으니까

