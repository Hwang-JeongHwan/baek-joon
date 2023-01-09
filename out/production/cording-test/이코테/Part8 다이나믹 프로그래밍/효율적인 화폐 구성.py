n, m = map(int, input().split())

# n 개의 화폐 단위 정보를 입력받기
array = []
for i in range(n):
    array.append(int(input()))
print(array)
# 한번 계산된 결과를 저장하기 위한 DP 테이블 초기화 
d = [10001] * (m + 1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0
# n개의 화폐 2, 3, 7 
# i = 각각의 화폐 단위
for i in range(n):
    # 화폐갯수, m원 까지
    # j = 각각의 금액 => 각각의 화폐단위를 하나씩 확인하면서 그 때에 대해 모든 금액을 확인하면
    # 각 금액에대한 옵티멀 솔루션값을 갱신할수있도록함 
    for j in range(array[i], m + 1):
        #print(d[j - array[i]])
        if d[j - array[i]] != 10001: #(i - k)원을 만드는 방법이 존재하는 경우 -> d[0] = 0로 초기화
            # d[j - array[i]] != 10001이면 j = 2 이고 array[i] = 2일대 d[2-2] = d[0] = 0이므로 성립
            d[j] = min(d[j], d[j - array[i]] + 1) # 초기에 j = 2이라면 
            # d[2] = 10001이고 min(d[2],d[0]+1) = d[0]+1 이므로 d[2] = 1
            # d[4] = 10001이고 min(d[4],d[2]]) = 10001>2 이므로 d[4] = 2

#print(d)
# 계산된 결과 출력
if d[m] == 10001: #최종적으로 M원을 만드는 방법이 없을경우
    print(-1)

else:
    print(d[m])

