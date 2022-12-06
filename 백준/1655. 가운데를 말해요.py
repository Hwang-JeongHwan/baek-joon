# 백준이가 정수를 하나씩 외칠떄마다 동생은 지금까지 백준이가 말한 수 중에서
# 중간 값을 말해야한다
# 만약 그 동안 백준이가 외친 수의 개수가 짝수라면 중간에 있는 두 수중에서
# 작은수를 말해야함

# ex 1 5 2 10 -99 7 5 를 순서대로 외쳤다면

import heapq
import sys
input = sys.stdin.readline
n = int(input())


left = []
right = []
for i in range(n):
    x = int(input())
    if len(left) == len(right):
        # max_heap
        heapq.heappush(left, (-x, x))
    else:
        heapq.heappush(right, (x, x))
    
    # 오른쪽 값에 원소가 있으면서,
    # 왼쪽 값이 오른쪽 값보다 큰 경우 left원소보다 right 원소가 더 커야한다는
    # 조건에 위배
    if right and left[0][1] > right[0][1]:
        left_value = heapq.heappop(left)
        #left_value = left_value[1]
        #위아래 같은 코드임 
        #left_value = heapq.heappop(left)[1]
        
        right_value = heapq.heappop(right)


        
        heapq.heappush(left, (-right_value[1], right_value[1]))
        heapq.heappush(right, (left_value[1], left_value[1]))
    print(left[0][1])
 