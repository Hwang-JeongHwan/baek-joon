n = input()
length = len(n) // 2

left_side = n[:length]
right_side = n[length:]
left = 0
right = 0
for i in range(length):
    left += int(left_side[i])
    right += int(right_side[i])

if left == right:
    print('LUCKY')
else:
    print('READY')
