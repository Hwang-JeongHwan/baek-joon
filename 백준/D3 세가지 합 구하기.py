# S1 = 양의 정수 중에서 작은 순서대로 N개의 합
# S2 = 양의 정수중 홀수인 것등중에서 작은 순서대로 N개의 합
# S3 = 양의 정수 중 짝수인 것들 중에서 작은 순서대로 N개의 합

tc = int(input())
result = []
data = []
for t in range(tc):
    n = int(input())
    data.append(n)

# for t in range(tc):
#     n = data[t]
#     count = 1
#     s1 = 0
#     s1_count = 1
#     s2 = 0
#     s2_count = 1
#     s3 = 0
#     s3_count = 2
#     count = 0
#     while True:
#         # print(s1)
#         s1 += s1_count
#         s2 += s2_count
#         s3 += s3_count
#
#         count += 1
#         s1_count += 1
#         s2_count += 2
#         s3_count += 2
#
#         if count == n:
#             break
#     result.append((s1,s2,s3))
for t in range(tc):
    n = data[t]
    # 전체 합 : n(n + 1) // 2
    # 홀수의 합: n ** 2
    # 짝수의 합: n(n + 1)
    result.append((((n * (n + 1)) // 2), (n ** 2), (n * (n + 1)) ))

for i in range(tc):
    print('#{} {} {} {}'.format(i + 1, result[i][0], result[i][1], result[i][2]))
