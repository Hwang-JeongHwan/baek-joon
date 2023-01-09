
data = input()
a = []
b = 0

for i in data:
    if i.isalpha():
        a.append(i)
    else:
        b += int(i)
        
a.sort()
if b != 0:
    a.append(str(b))
# 공백없이 리스트에 포함된 문자를 문자열로 변환하여 출력 
print(''.join(a))
