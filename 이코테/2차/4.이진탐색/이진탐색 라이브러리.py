# # 코딩테스트를 풀기위해 알아두면 좋은 이진탐색 라이브러리

#  bisect_left(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를
#  반환

#  bisect_right(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽
#  인덱스를 반환

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x)) # 정렬된 순서를 유지하면서 x를 집어넣을때 x가 갈수있는
# 가장 왼쪽 인덱스
print(bisect_right(a, x)) # 정렬된 순서를 유지하면서 x를 집어넣을때 x가 갈수 있는
# 가장 오른쪽 인덱스
