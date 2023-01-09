# 순차 탐색: 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는
# 방법

# 이진탐색: 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는
# 방법

# 이진탐색읕 시작점 끝점 중간점을 이용하여 탐색범위를 설정함

# 단계마다 탐색 범위를 2로 나누는것과 동일하므로 연산 횟수는 log2N 에 비례함
# 예를 들어 초기 데이터 개수가 32개 일대 이상적으로 1단계를 거치면 16개 가량의 데이터만
# 남음

# 2단계를 거치면 8개 가량의 데이터만 남음
# 3단계를 거치면 4개 가량의 데이터만 남음

# 다시말해 이진탐색은 탐색 범위를 절반씩 줄이며 시간복잡도는 O(logN)을 보장함

# 이진탐색 소스코드 구현(재귀 함수)

def binary_search(array, target, start, end):
    if start > end:
        print('no',end, start)
        return None
    mid = (start + end) // 2

    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    if array[mid] > target:
        # print('start, end - 1', start, mid - 1)
        return binary_search(array, target, start, mid - 1)
    else:
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        # print('mid + 1, end',mid + 1, end)
        return binary_search(array, target, mid + 1, end) # 여기서 return을 안하면 
        # 재귀함수 호출하고 난뒤 끝날때 None을 return 해버림
        # 그래프 만지는 DFS같은경우 return을 안해줘도 되는게 return 받는 값을 가지고
        # 프로그래밍하는게 아니라 그래프의 값만 바꿔주면되니까 return같은걸 안해줫던
        # 거였음 재귀함수를 사용하면서 값이 필요한경우 return해주어야함 


n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
print('re', result)
if result == None:
    print('원소가 존재하지 않습니다')
else:
    print(result + 1)