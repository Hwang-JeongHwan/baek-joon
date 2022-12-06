# 우선순위 큐:

# 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조

# 예를 들어 여러개의 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건
# 데이터부터 꺼내서 확인해야 하는 경우 우선순위 큐를 이용할수 있음

# stack : 가장 나중에 삽입된 데이터 부터 추출
# queue: 가장 나중에 삽입된 데이터 부터 추출
# priority queue: 가장 우선순위가 높은 데이터


# heap :우선 순위 큐를 구현하기 위해 사용하는 자료구조중 하나
# 최소 힙(Min Heap)과 최대 힙(Max Heap)이 있음

# 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 사용됨

# 우선순위 큐 구현 방식       삽입시간        삭제시간
# 리스트                      O(1)            O(N)
# 힙(Heap)                    O(logN)         O(logN)

# 힙 라이브러리 사용 예제 : 최소 힙 우선순위가 낮은 데이터부터 수행
import heapq
# 오름차순 힙 정렬(Heap Sort) 최소 힙 정렬
def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)

    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# 내림차순 힙 정렬
def max_heapsort(iterable):
    h = []
    result = []
    # 데이터를 넣을때 - 를 붙여서 넣어줌
    for  value in iterable:
        heapq.heappush(h, -value)
    
    for i in range(len(h)):
        # 꺼낸 데이터에 - 를 붙여줌 
        result.append(-heapq.heappop(h))
    return result

result1 = max_heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result1)