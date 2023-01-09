# def binary_search_loop(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
        
#         elif array[mid] > target: # elif 로 안하면 else가 array[mid] <= target이렇게 됨
#             # 근데 이래도 상관없는거같은에 위에서 == 하고 return 하니까..?

#             end = mid - 1
#         else:
#             start = mid + 1
        
#     return None

# 절단기 높이는 0부터 10억 이렇게 범위가 넓으면 이진탐색을 먼저 생각해야함

# 시작점 = 0 끝점은 data의 가장 큰수로 설정


# def find(array, target, start, end):
#     mid = (start + end) // 2
#     sum = 0
#     if start > end:
#         return False
#     for i in range(len(array)):
#         if array[i] >= mid:
#             sum += array[i] - mid

#     if sum == target:
#         return mid
#     if sum > target: # mid 값이 더 커져야함 그러므로 start를 늘려줘야함
#         return find(array, target, mid + 1, end)
#     else:
#         return find(array, target, start, mid - 1)
# 적어도 m만큼이니까 각각의 떡 길이를 합친게 m 이랑 크거나 같으면됨
# 위에 처럼 하면 딱 m 만큼임

def find(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        total  = 0
        for i in array:
            if i - mid > 0:
                total += i - mid
        
        if total < target: # 길이를 줄여줘야함
            end = mid - 1
        else:
            result = mid # 최대한 덜 잘랐을때가 답이므로result에 mid값 저장
            start = mid + 1
    return result

            



n, m = map(int, input().split())
array = list(map(int, input().split()))
start = 0
end = max(array)
print(find(array, m, start, end))


while start <= end:
    mid  = (start + end) // 2
    total = 0
    for i in array:
        if i - mid > 0:
            total += i - mid

    # if total >= m:
    #     result = mid
    #     start = mid + 1
    # else:
    #     end = mid - 1
    if total < m :
        end = mid - 1
    else:
        start = mid + 1
        result = mid 

print(result)

