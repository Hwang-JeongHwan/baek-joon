#큐는 먼저들어온 데이터가 먼저나가는 선입선출 형태임
# 입구와 출구가 모두 둘려있는 터널과 같은 형태 -> 은행 창구 같은곳
# 대기열// 먼저들어온 데이터가 먼저 처리 받는 형태

#리스트 자료형으로 구현하면 시간복잡도가 높음
from collections import deque
#deque 라이브러리 사용

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #먼저들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue) #나중에 들어온 원소부터 출력 