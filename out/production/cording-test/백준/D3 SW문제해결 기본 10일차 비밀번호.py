for t in range(1, 11):
    stack = []
    n, s = input().split()
    n = int(n)
    nums = list(s)

    for i in range(n):
        if not stack:
            stack.append(nums[i])
        else:
            if stack[-1] == nums[i]:
                stack.pop()
            else:
                stack.append(nums[i])


    print('#{} {}'.format(t, ''.join(stack)))


# for t in range(1, 11) :
#     N, string = input().split()
#     N = int(N)
#     string = list(string)

#     i = 0
#     while(True) :
#         if string[i] == string[i+1] :
#             del(string[i:i+2])
#             N -= 2
#             i -= 2
#         i += 1
#         if i == (N-1) :
#             break

#     password = ''
#     for i in range(N) :
#         password += string[i]

#     print("#{} {}".format(t, password))