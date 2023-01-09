n = input()

x = len(n) // 2

left = 0
right = 0
for i in range(x):
    left += int(n[i])

for j in range(x, len(n)):
    right += int(n[j])


if left == right:
    print('LUCKY')
else:
    print('READY')