n = int(input())
array = list(map(int, input().split()))

odd = 0
even = 0
for i in range(n):
    if i % 2 == 0:
        even += array[i]
    else:
        odd += array[i]

print(odd,even)
print(max(odd,even))