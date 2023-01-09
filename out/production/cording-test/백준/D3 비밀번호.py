tc = 10
for t in range(1, tc + 1):
    n, s = input().split()

    stack = []
    for i in range(int(n)):
        # print(stack, s[i])
        if stack and s[i] == stack[-1]:
            stack.pop()
            continue
        
        stack.append(s[i])


    print('#{} {}'.format(t, ''.join(stack)))
    