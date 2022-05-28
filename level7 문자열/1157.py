'''
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다
'''

S = input().upper()
S_list = list(set(S))
# 중복을 제거하기 위해 set으로 만듬 
cnt = []

for i in S_list:
    count = S.count(i) #count함수는 i의 갯수를 세어줌
    #입력받은 문자열안에 i가 몇개있는지 세어줌
    cnt.append(count)
'''
    print('count',count,i)

print('s',S_list)
print('cnt',cnt)
print('cnt.index(max(cnt)',cnt.index(max(cnt)))
'''
if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(S_list[cnt.index(max(cnt))])
