data = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet',
'grey', 'white']
# print(data)

x = input()
y = input()
z = input()

result = 0
mul = 0
for i in range(len(data)):
    if data[i] == x:    
        result = result + (i * 10)
    if data[i] == y:
        result += i
    if data[i] == z:
        if data[i] == 'black':
            mul = 1
        else:
            mul = (10 ** i)

print(10 ** 0)
print(result * mul)
