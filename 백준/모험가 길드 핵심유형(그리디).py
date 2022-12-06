'''
문제 정의

한 마을에 모험가가 N명 있다. 모험가 길드에서는 N명의 모험가를 대상으로 공포도를 측정했는데, 공포도가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어진다.

 

모험가 길드장인 동빈이는 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했다.

 

동빈이는 최대 몇 개의 모험가 그룹을 만들 수 있는 지 궁금하다. N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하시오.

 

입력

첫째 줄에 모험가의 수 N이 주어진다. (1 ≤ N ≤ 100,000)

둘째 줄에 각 모험가의 공포도의 값을 N 이하의 자연수로 주어지며, 각 자연수는 공백으로 구분한다.

 

출력

여행을 떠날 수 있는 그룹 수의 최댓값을 출력한다.

 

예제 입력 1

5
2 3 1 2 2
예제 출력 1

2
'''

n = int(input())
data = list(map(int, input()))

data.sort()

result = 0
count = 0 # 현재 그룹에 포함된 모험가의 수
for i in data:
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i : #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면
        # 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화 

print(result)