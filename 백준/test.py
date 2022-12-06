def solution(v):
    answer = []
    count_x = []
    count_y = []
    x = 0
    y = 0
    for i in range(len(v)):
        count_x.append(v[i][0])
        count_y.append(v[i][1])

    for i in range(len(count_x)):
        if count_x.count(count_x[i]) == 1:
            x = count_x[i]
        if count_y.count(count_y[i]) == 1:
            y = count_y[i]
    answer.append(x)
    answer.append(y)
    return answer

v = [[1,4],[3,4],[3,10]]
print(solution(v))