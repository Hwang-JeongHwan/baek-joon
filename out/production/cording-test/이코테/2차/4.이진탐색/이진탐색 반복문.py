def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        # 중간점이 찾고자 하는 값보다 크면 즉 찾고자하는 값이 중간점보다 작다면
        # end의 범위를 좁혀줌 
        if array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    # start > end : return none
    return None
n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print('원소가 존재하지 않습니다')
else:
    print(result + 1)

# def binary_search1(array, target, start, end):
#     mid = (start + end) // 2
#     if array[mid] == target:
#         return None
    
#     if array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
#     else:
#         return binary_search(array, target, mid + 1, end)