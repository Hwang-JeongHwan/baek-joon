# # https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AV6kld8aisgDFASb&contestProbId=AV15FZuqAL4CFAYD&probBoxId=AV-4MojKLNADFATz&type=PROBLEM&problemBoxTitle=%5BD2%7ED3+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%5D+%EA%B8%B0%EC%B4%88+%EB%8B%A4%EC%A7%80%EA%B8%B0+Part4&problemBoxCnt=14
# # 홀수 자리의 합 * 3  + 짝수 자리의 합이 10의 배수가 되어야함

# code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011','0110111','0001011']

# tc = int(input())
# for t in range(1, tc + 1):
#     n, m = map(int, input().split())
#     data = []
#     for i in range(n):
#         input_data = input()
#         data.append(input_data)

#     new = ''

#     for i in range(n):
#         if sum(map(int, list(data[i]))) == 0:
#             continue
#         else:
#             now = data[i]
#             # print(now)
#             for j in range(m - 1, -1, -1):
#                 # print('now', j, now[j])
#                 if now[j] == '1':
#                     new = now[j - 55 : j + 1]
#                     # print('new', new)
#                     break
#             break
#     result = []
#     for i in range(0, len(new) ,7):
#         result.append(new[i : i + 7])
#     answer = []

#     for j in range(len(result)):
#         answer.append(code.index(result[j]))
#     odd = 0
#     even = 0
#     flag = True
#     # print(result)
#     for j in range(len(answer)):
#         if j % 2 == 0:
#             odd += answer[j]
#             flag = False
#         else:
#             even += answer[j]

    
        
#     if ((odd * 3) + even) % 10 == 0:

#         print('#{} {}'.format(t, odd + even))
#     else:
#         print('#{} {}'.format(t, 0))
            
            

#     # falg = False
#     # for i in range(0, len(result), 8):
#     #     even = 0
#     #     odd = 0  
#     #     for j in range(8):
  
#     #         if (i + j) % 2 == 0:
#     #             if i + j < len(result):
#     #                 even += result[i + j]
#     #             # print('even', even)
#     #         else:
#     #             if i + j < len(result):
#     #                 odd += result[i + j]
#     #             # print('odd', odd)
#     #     if ((even * 3) + odd) % 10 == 0:
#     #         print('#{} {}'.format(t, odd + even))
#     #         falg = True
#     #         break
#     # even = 0
#     # odd = 0
#     # print(len(result))
#     # for i in range(len(result)):
#     #     if i % 2 == 0:
#     #         odd += result[i]
#     #     else:
#     #         even += result[i]
        
    
        
#     # if ((odd * 3) + even) % 10 == 0:

#     #     print('#{} {}'.format(t, odd + even))
#     # else:
#     #     print('#{} {}'.format(t, 0))
            

my_dict = {'0001101': 0, '0011001': 1,
           '0010011': 2, '0111101': 3,
           '0100011': 4, '0110001': 5,
           '0101111': 6, '0111011': 7,
           '0110111': 8, '0001011': 9}

tc = int(input())
for t in range(1, tc + 1):
    n, m = map(int, input().split())
    data = []
    for i in range(n):
        input_data = input()
        data.append(input_data)

    new = ''

    for i in range(n):
        if sum(map(int, list(data[i]))) == 0:
            continue
        else:
            now = data[i]
            # print(now)
            for j in range(m - 1, -1, -1):
                # print('now', j, now[j])
                if now[j] == '1':
                    new = now[j - 55 : j + 1]
                    # print('new', new)
                    break
            break
    result = []
    for i in range(0, len(new) ,7):
        result.append(new[i : i + 7])
    answer = []
    # print(result)

    for j in range(len(result)):
        answer.append((my_dict[result[j]]))
    odd = 0
    even = 0
    flag = True
    # print(result)
    for j in range(len(answer)):
        if j % 2 == 0:
            odd += answer[j]
            flag = False
        else:
            even += answer[j]

    
        
    if ((odd * 3) + even) % 10 == 0:

        print('#{} {}'.format(t, odd + even))
    else:
        print('#{} {}'.format(t, 0))
            
            