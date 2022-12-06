def solution(N, stages):
    answer = []
    length = len(stages)

    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N + 1):
        # fail = stages.count(i) / length 애초에 이렇게 하면 0으로 나누는 경우가 생겨
        # runtime error가 발생함 ZeroDivisionError 발생 !
        if length == 0:
            fail = 0
        else:
            fail = stages.count(i) / length    
        # # 해당 스테이지에 머물러 있는 사람의 수 계산
        # count = stages.count(i)
        
        # # 실패율 계산
        # if length == 0:
        #     fail = 0
        # else:
        #     fail = count / length
        
        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= stages.count(i)
    print(answer)
    result = []
    answer.sort(key = lambda x: -x[1])
    for i, j in answer:
        result.append(i)
    return result

n = 5
stages = [2, 2, 2, 2, 2, 2, 2, 2]
print(solution(n, stages))