# 탐색(Search)란 많은양의 데이터중에서 원하는 데이터를 찾는 과정을 말함
# 대표적인 그래프 탐색 알고리즘으로는 DFS와 BFS가 있음
# DFS/BFS는 코딩테스트에서 매우 자주 등장하는 유형이므로 반드시 숙지해야함


# 스택 자료구조

# 먼저들어온 데이터가 나중에 나가는 형식(선입후출)의 자료구조
# 입구와 출구가 동일한 형태로 스택을 시각화 할 수 있음 

# 스택 구현 예제
stack = []
# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력 

# 큐 자료구조

# 먼저 들어온 데이터가 먼저 나가는 형식(선입선출)의 자료구조
# 큐는 입구와 출구가 모두 뚫려있는 터널과 같은 형태로 시각화 할 수 있음
# 대기열이라고 볼수있음 

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()

from collections import deque
# 큐(Queqe) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()
print(queue)
# 역순으로 출력, ::-1 형식으로는 안됨! 
queue.reverse()
print(queue)
