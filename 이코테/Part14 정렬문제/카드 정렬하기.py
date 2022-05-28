import heapq
n = int(input())

# 힙(Heap)에 초기 가드 묶음을 모두 삽입
heap = []

for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)
    # 50 40 20 10 으로 입력하면
    # 10 20 40 50 순으로 들어가짐 지절로
#print(heap)

result = 0

# 힙(Heap) 원소가 1이 남을때 까지
while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_value = one + two
    result += sum_value
    
    heapq.heappush(heap,sum_value)
    #print(heap)

print(result)
