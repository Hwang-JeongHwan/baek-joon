# insert = 삽입
# remove = 삭제
# replace = 교체

# len(a) == len(b) => 교체
# len(a) > len(b) => 삭제
# len(a) < len(b) => 삽입

# 같은 문자가 몇개 있는지 파악 -> 

a = input()
b = input()



x = 0
y = 0
if len(a) == len(b):
    x = len(a)
    y = len(b)

elif len(a) > len(b):
    x = len(a)
    y = len(b)

else:
    x = len(b)
    y = len(a)
    a, b = b, a

same = 0
for i in range(x):
    for j in range(y):
        if a[i] == b[j]:
            same += 1
            break
print(x - same)

