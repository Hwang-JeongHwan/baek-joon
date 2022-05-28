n = int(input())
result = []
for i in range(1, n + 1):
    count = 0
    for j in str(i):
        if '3' in str(j):
            count += 1
        if '6' in str(j):
            count += 1
        if '9' in str(j):
            count += 1

    if count > 0 :
        result.append('-' * count)
    else:
        result.append(str(i))

print(' '.join(result))
