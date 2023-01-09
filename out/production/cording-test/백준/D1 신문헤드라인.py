data = list(input())
for i in range(len(data)):
    if data[i].isalpha():
        data[i] = data[i].upper()

for i in data:
    print(i, end='')