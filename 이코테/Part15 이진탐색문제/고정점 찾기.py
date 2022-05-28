# 시간 복잡도 O(logN) = 이진탐색 선형 탐색 = O(N)

def binary_search(array,start,end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input())
data = list(map(int, input().split())) 

index = binary_search(data,0,n-1)

if index == None:
    print(-1)
else:
    print(index)