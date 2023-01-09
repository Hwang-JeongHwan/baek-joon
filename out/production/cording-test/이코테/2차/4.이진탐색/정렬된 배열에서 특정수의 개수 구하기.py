from bisect import bisect_left, bisect_right

n, x = map(int, input().split())

array = list(map(int, input().split()))

if x not in array:
    print(-1)
else:
    print(bisect_right(array, x) - bisect_left(array, x))

def find(array, x):
    left = bisect_left(array, x)
    right = bisect_right(array , x)

    return right - left

print(find(array, x))