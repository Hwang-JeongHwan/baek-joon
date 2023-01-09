def solution(N, stages):
    result = [0] * (N + 2)
    x = len(stages)
    for i in stages:
        result[i] += 1
    answer1 = []
    print(result)
    for i in range(1, len(result) - 1):
        if x == 0:
            fail = 0
        else:
            fail = result[i]/x
        answer1.append((i, fail))
        
        x -= result[i]

    answer = []
    answer1.sort(key = lambda x: -x[1])
    for i,j in answer1:
        answer.append(i)


    return answer

N = 4
stages = [4, 4, 4, 4, 4]
# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N,stages))