# https://school.programmers.co.kr/learn/courses/30/lessons/42891

def solution(food_times, k):
    total_times = sum(food_times)
    i = 0

    length = len(food_times)
    for j in range(total_times):
        if food_times[i] > 0 :
            food_times[i] -= 1

        i += 1
            
            
        if i == length:
            i = 0
        
        if j == k:
            if sum(food_times) > 0:
                return i + 1
            else:
                return -1
            

    return -1


food_times = [3, 1, 2]
k = 5

print(solution(food_times, k))
# ㅈㅈ
# 나중에 답지보자..
