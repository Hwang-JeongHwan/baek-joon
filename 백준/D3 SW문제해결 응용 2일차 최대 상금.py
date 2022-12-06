# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV15Khn6AN0CFAYD&probBoxId=AV-4MojKLNADFATz&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part4&problemBoxCnt=14


# def dfs(index, count):
#     global result 
#     if count == k:
#         result = max(int(''.join(data)), result)
#         return

#     for i in range(index, len(data)):
#         for j in range(i + 1, len(data)):
#             if data[i] <= data[j] :
#                 data[i], data[j] = data[j], data[i]
#                 dfs(i, count + 1)
#                 data[i], data[j] = data[j], data[i]
#     if result == 0 and count < k :
#         extra = (k - count) % 2
#         # 짝수라면 그대로, 홀수라면 한 번 변경
#         if extra == 1 : # 홀수라면
#             data[-1], data[-2] = data[-2], data[-1]
#         dfs(index, k)

# tc = int(input())
# for t in range(1, tc + 1):
#     s, k = input().split()
#     k = int(k)
#     result = 0
#     data = list(s)

#     dfs(0, 0)
    
#     print('#{} {}'.format(t, result))

def dfs(count):
    global result
    # print(result, data)
    if count == k:
        temp = ''.join(data)
        if result < temp:
            result = temp
        return
    
    for i in range(length):
        for j in range(i + 1, length):
            if data[i] <= data[j]:
                data[i], data[j] = data[j], data[i]
                temp = ''.join(data) 
                # print('t',temp)
                if visited.get((temp, count), 1):
                    visited[(temp, count)] = 0
                    dfs(count + 1)
                data[i], data[j] = data[j], data[i]               


tc = int(input())
for t in range(1, tc + 1):
    s, k = input().split()
    k = int(k)
    result = '0' 

    data = list(s)
    length = len(data)
    visited = {}
    dfs(0)
    
    print('#{} {}'.format(t, result))

def dfs(count):
    global result
    if count == k:    # n만큼 바꿔줬다면
        temp = ''.join(data)   # 문자열로 바꿔주기
        if result < temp:   # answer에 저장되어있는 값보다 크다면 갱신
            result = temp
        return
 
    for i in range(len(s)):
        for j in range(i + 1, len(s)): # 현재 자리(i)의 다음자리부터 비교
            data[i], data[j] = data[j], data[i] # 바꾸기
            temp = ''.join(data)               # 문자열로 바꿔
            if visited.get((temp, count), 1):     # 중복 아니라면
                visited[(temp, count)] = 0        # visited에 저장
                dfs(count + 1)                 # 들어가기
            data[i], data[j] = data[j], data[i] # 원상복귀
 
 
tc = int(input())
for t in range(1, tc + 1):
    s, k = input().split()
    k = int(k)
    data = list(s)
    visited = {}            # 중복 방지 딕셔너리
    result = '0'     # 정답 담는 변수 초기화
 
    dfs(0)
 
    print('#{} {}'.format(t, result))
