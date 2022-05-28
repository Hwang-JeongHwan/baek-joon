N,M,K = map(int, input().split())

a = list(map(int, input().split()))

a.sort()

x = a[N-1]
y = a[N-2]
count = 0 
total = 0
for i in range(1,M+1):
    if i%K == 0 : #i가 K의 배수면
        total += y #두 번째로 큰수를 더하고
        count +=1
    else:
        total += x #i가 K의 배수가 아니면 첫번째로 큰수를 더함
        count +=1


print(total,count)
while True:
    for i in range(K): #가장 큰 수를 K번 더하기
        if M == 0: # M이 0이라면 반복문 탈출
            break
        total += x
        M -= 1 # 더할 떄 마다 1씩 빼기
    if M == 0: # M이 0이라면 반복문 탈출
        break
    total += y # 두 번째로 큰수를 한 번 더하기
    M -= 1 # 더할 떄 마다 1씩 빼기
print(total)