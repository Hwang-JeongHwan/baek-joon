import sys
input = sys.stdin.readline

n, c = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))
#1 2 4 8 9
start = 1 # 가능한 최소 거리, 1
array.sort()
end = array[n - 1] - array[0] # 가능한 최대거리 , 8

result = 0

while start <= end:
    count = 1
    # 첫번째 집은 무조건 공유기를 설치한다고 가정
    first = array[0] # 1
    
    mid = (start + end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리를 의미

    for i in range(1, n):
        if array[i] >= mid + first:
            count += 1
            first = array[i]

   
    if count >= c: # c 개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가시키기
        start = mid + 1
        result = mid # 최적의 결과 저장

    else: # c개 이상의 공유기를 설치할 수 없는경우 거리 감소시키기
        end = mid - 1

print(result)
'''
집을 정렬해서 최소 거리와 최대 거리를 계산하고 이들의 중간값을 계산
중간값을 기준으로 집의 개수를 셌을 때 C보다 크다면, 최소값을 중간값 + 1로 갱신하고,
중간값을 기준으로 집의 개수를 셌을 때 C보다 작다면, 최댓값을 중간값 - 1로 갱신한다.
이걸 계속 반복하는 데, 최솟값과 최댓값이 같아질 때까지 반복한다.
근데 내 궁금증은 이진 탐색은 “찾고자 하는 값”을 빨리 찾고자 하기 위한 알고리즘인데 이게 어떻게 공유기 설치 문제에 적용되는 지이다. 공유기 설치 문제의 목적은 C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 것인데…

초기값 = 중간값: 특정 간격을 기준으로 가능한 위치에 공유기를 설치한다.
설치한 후에는 다음과 판단한다.
공유기 수가 더 설치되어야 한다면, 간격을 줄인다.
공유기 수를 줄여야한다면, 간격을 늘린다.
결국 최대 간격은 최대 중간값에 해당하는 것 같다!


'''