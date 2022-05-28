data = input()
result = []
value = 0
# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
    
result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))
# for i in data:
#     print(i,end='')

# # 원본 리스트
# a = ['BlockDMask', 'python', 'join', 'example']
# print(a)
# print()
 
# # 리스트를 문자열로 합치기
# result1 = "_".join(a)
# print(result1)
 
# # 리스트를 문자열로 합치기
# result2 = ".".join(a)
# print(result2)
