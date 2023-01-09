n = int(input())

array = []

for i in range(n):
    data = input().split()
    #print(data)
    array.append((data[0], data[1]))

array.sort(key = lambda x:x[1])
# array = sorted(array, key = lambda student: student[1])

# for i in range(len(array)):
#     print(array[i][0],end=' ')
for student in array:
    print(student[0],end=' ')