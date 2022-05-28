def solution(n, food_times, k):
    count = 0
    i = 0
    x = 0
    while x < k:
        if i == n:
            i -= n
        count += 1
        x += 1
        food_times[i] -=1
        if food_times[i] <= 0:
            count += 1
        if count > n:
            count -= n
        i += 1    
    if max(food_times) <= 0:
        return -1
    return count

n = int(input())
food_times = list(map(int, input().split()))
k = int(input())

print(solution(n, food_times, k))