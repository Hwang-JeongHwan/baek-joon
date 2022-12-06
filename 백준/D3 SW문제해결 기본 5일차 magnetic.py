# tc = 10

# def solution_N(x, y):
#     if x + 1 >= n:
#         return
#     if data[x + 1][y] == 0:
#         data[x + 1][y] = 1
#         data[x][y] = 0
#         solution_N(x + 1, y)
# def solution_S(x, y):
#     if x - 1 < 0:
#         return
    
#     if data[x - 1][y] == 0:
#         data[x - 1][y] = 2
#         data[x][y] = 0
#         solution_S(x - 1, y)


# for t in range(1, tc + 1):
#     n = int(input())
#     data =[]
#     for i in range(n):
#         data.append(list(map(int, input().split())))
    
#     for i in range(n):
#         for j in range(n):
#             if data[0][j] == 2 and data[1][j] != 1:
#                 data[0][j] = 0

#             if data[n - 1][j] == 1 and data[n - 2][j] != 2:
#                 data[n - 1][j] = 0
            
#             if data[j][i] == 1:
#                 solution_N(j, i)
#             if data[j][i] == 2:
#                 solution_S(j, i)
#     print(data)
#     count = 0
#     for i in range(n):
#         for j in range(n - 1):
#             if j + 2 <= n - 1:
#                 if data[j][i] == 1 and data[j + 1][i] == 2 and data[j + 2][i] == 0:
#                     count += 1
#             else:
#                 if data[j][i] == 1 and data[j + 1][i] == 2:
#                     count += 1
#     print('#{} {}'.format(t, count))
# for t in range(1, tc + 1):
#     n = int(input())

#     # data = []
#     # for i in range(n):
#     #     data.append(list(map(int, input().split())))
    
#     # for i in range(n):
#     #     k = n - 1
#     #     for j in range(n):
#     #         if data[0][j] == 2 and data[1][j] != 1:
#     #             data[0][j] = 0

#     #         if data[n - 1][j] == 1 and data[n - 2][j] != 2:
#     #             data[n - 1][j] = 0

#     #         if  j + 1 < n :
#     #             if data[j][i] == 1 and data[j + 1][i] == 0:
#     #                 data[j][i] = 0
#     #                 data[j + 1][i] = 1
            
#     #         if k > 0:
#     #             if data[k][i] == 2 and data[k - 1][i] == 0:
#     #                 data[k][i] = 0
#     #                 data[k - 1][i] = 2
#     #         k -= 1
#     #         if k == -1:
#     #             break
    
#     # count = 0
#     # for i in range(n):
#     #     for j in range(n - 1):
#     #         if j + 2 <= n - 1:
#     #             if data[j][i] == 1 and data[j + 1][i] == 2 and data[j + 2][i] == 0:
#     #                 count += 1
#     #         else:
#     #             if data[j][i] == 1 and data[j + 1][i] == 2:
#     #                 count += 1
#     # print('#{} {}'.format(t, count))

# for t in range(1, 11):
#     n = int(input())
#     data = []
#     for i in range(n):
#         data.append(list(map(int, input().split())))

#     count = 0
#     result = []

#     for i in range(n):
#         before = data[0][i]
#         for j in range(n):
#             if data[j][i] == 0:
#                 continue

#             if before == 1 and data[j][i] == 2:
#                 count += 1
#             before = data[j][i]
#     print('#{} {}'.format(t, count))        
for t in range(1, 11):
    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))

    count = 0
    for i in range(n):
        stack = []
        for j in range(n):
            if data[j][i] == 1:
                stack.append(1)
            
            if stack and data[j][i] == 2:
                stack.clear()
                count += 1

    print('#{} {}'.format(t, count))        
