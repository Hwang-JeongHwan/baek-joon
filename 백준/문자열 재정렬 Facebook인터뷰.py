s = input()

alpha = ''
num = 0
for i in range(len(s)):
    if s[i].isalpha():
        alpha += s[i]
    else:
        num += int(s[i])
array = list(alpha)
array.sort()
if num != 0:
    array.append(str(num))
print(''.join(array))