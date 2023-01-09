# n = int(input())
# length = 64
# count = 1
# result = []
#
# result.append(64)
# while True:
#     # print(result)
#     if sum(result) > n:
#         x = result[-1] // 2
#         # print('x', x)
#         if sum(result) - x >= n:
#
#             result.pop()
#             # print('pop',result)
#             result.append(x)
#             # print('append',result)
#         else:
#             result[-1] //= 2
#             result.append(x)
#     # print(result)
#     if sum(result) == n:
#         break
#
#     # count += 1
#
#
# print(len(result))
#
# # 1094번

x = int(input())

stick = [64, 32, 16, 8, 4, 2, 1]
count = 0

for i in range(len(stick)):
    if x >= stick[i]:
        count += 1
        x -= stick[i]
    print(x, i, stick[i])
    if x == 0:
        break

print(count)
'''
만들 수 있는 막대기의 모든 길이를 처음부터 stick이라는 리스트에 담아둔다.

 

큰 막대기부터 x와 비교해서 x가 더 크다면 그 막대기를 붙이고 x는 그 막대기의 길이만큼 빼준다.

 

남은 길이만큼을 다시 나머지 막대기들과 비교해서 x가 0이 될때까지 막대기를 붙인다.

 

x가 0이되면 반복문을 종료하고 몇개의 막대기를 붙였는지 출력한다.

 

예를들어 x의 길이가 23cm이라면 x를 만들기 위해선 64cm와 32cm는 너무 큰 막대기일 것이다.

 

16cm은 23cm보다 작기 때문에 16cm을 붙이고나면 x만큼 되기 위해선 7cm가 남는다.

 

8cm짜리 막대기는 7cm보다 크기 때문에 안되고 4cm짜리 막대기를 붙여준다.

 

이제 3cm가 남았기 때문에 2cm와 1cm막대기를 붙여주면

 

23cm = 16cm + 4cm + 2cm + 1cm로 총 4개의 막대기가 필요한 것이다.'''
a = int(input())
cnt = 0
while a != 0:
    if a % 2 == 1:
        cnt += 1
    a = a // 2
print(cnt)
# 길이가
# 64, 32, 16, 8, 4, 2, 1 짜리 막대를 최소 몇개 붙여야 하나 하는 문제이다.
# 2 진법으로 나타냈을때 1 이 몇개 있냐는 소리이다.
# 예를 들어 5 같은 경우 이진법으로 나타내면 101 이다. 1 이 2 개 있으므로 답은 2 이다.
# 23 같은 경우 이진법으로 나타내면 10111 이다. 1 이 4 개 있으므로 답은 4.