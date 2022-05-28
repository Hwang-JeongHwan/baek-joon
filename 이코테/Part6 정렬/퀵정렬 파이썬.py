array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
# 7<->4
# 5 4 9 0 3 1 6 2 7 8
# 9<->2
# 5 4 2 0 3 1 6 9 7 8
# 6<->1
# 1 4 2 0 3 5 6 9 7 8 
#

def quick_sort(array):
    print('len(array)',len(array))
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    print('left_side',left_side)
    print('right_side',right_side)
    print(left_side+[pivot]+right_side)

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환 
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))