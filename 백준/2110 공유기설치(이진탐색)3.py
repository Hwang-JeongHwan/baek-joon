import sys
input = sys.stdin.readline

def find(array, start, end):
    result = 0
    #print(n, c)
    while start <= end:
        count = 1
        mid = (start + end) // 2 # 인접한 두점의 거리를 가정
        first = array[0]
        for i in range(1, n):
            #print(array[i])
            if array[i] >= first + mid:
                first = array[i]
                count += 1
                #print(count)
        if count >= c: # 공유기를 많이 놓을수 있으니까 mid값을 증가 시키기 위해
            # start를 증가시킴
            result = mid
            start = mid + 1
        else: # c개 이상 설치할수 없는경우 , 거리를 감소 시키기 mid를 감소시키기
            end = mid - 1


    return result    


n, c = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

start = 1 # 두 집간의 최소 거리
end = array[-1] - array[0] # 두 집간의 최대 거리

print(find(array, start, end))
