def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 설치된 것이 '기둥' 인 경우
            if y == 0 or [x, y - 1, 0] in answer or [x, y, 1] in answer or [x - 1, y, 1] in answer:
                continue
            else:
                return False
            
        elif stuff == 1: # 설치된 것이 '보' 인 경우
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or [x - 1, y, 1] in answer and [x + 1, y, 1] in answer:
                continue
            else:
                return False


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0: # 삭제하는 거면
            answer.remove([x, y, stuff]) # 일단 지우고
            if possible(answer) == False : # 지울수 없다면
                answer.append([x, y, stuff]) # 다시 집어 넣음

        if operate == 1:
            answer.append([x, y, stuff]) # 일단 집어 넣고
            if possible(answer) == False: # 넣을수 없다면
                answer.remove([x, y, stuff])

    answer.sort()
    return answer
    
n = 5 
build_frame =[
    [0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]

print(solution(n, build_frame))