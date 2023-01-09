# 파이썬의 장점을 살린방식의 퀵정렬


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0] # 피벗은 첫번째 원소
    tail = array[1:] # 피벗을 제외한 원소

    left_side = [x for x in tail if x <= pivot] # tail에서 pivot 보다 작거나 같은
    # 원소들을 분할된 왼쪽 부분에 넣어줌

    right_side = [x for x in tail if x > pivot] # tail 에서 pivot보다 큰애들만
    # 분할된 오른쪽 부분에 넣어줌
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
print(array)
print(quick_sort(array))
print(array)


