def solution(N, stages):
    answer = []
    length = len(stages)

    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N + 1):
        count = stages.count(i)

        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length
        
        # 리스트에(스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count

    
    answer = sorted(answer, key = lambda x: x[1], reverse=True)

    # 정렬된 스테이지 번호 출력
    answer = [i[0] for i in answer]
    return answer
# N = 4
# stages = [4, 4, 4, 4, 4]
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N,stages))