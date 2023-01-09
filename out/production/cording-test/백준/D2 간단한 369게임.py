n = int(input())
print('-' * 2)

array = [i for i in range(n + 1)]

for i in range(1, n + 1):
    s = str(i)
    count = 0
    for j in range(len(s)):
        
        if '3' in s[j] or '6' in s[j] or '9' in s[j]:
            count += 1

        if count == 1:
            array[i] = '-'
        if count == 2:
            array[i] = '--'
        if count == 3:
            array[i] = '---'    

for i in range(1, n + 1):
    print(array[i], end=' ')