from collections import Counter

N = int(input())
a = []

for i in range(N):
    x = int(input())
    a.append(x)

a.sort()

print(round(sum(a)/N))
print(a[int(N/2)])




#Counter  함수를 쓰면 딕셔너리 형태로 저장
#most_common으로 하면 리스트 형태의 튜플값으로 저장
'''
counter = Counter(a)
counter Counter({-2: 1, 1: 1, 2: 1, 3: 1, 8: 1}) 
counting_array [(-2, 1), (1, 1), (2, 1), (3, 1), (8, 1)]   

'''

counting_array = Counter(a).most_common()
if N == 1:
    print(counting_array[0][0])
else:
    if counting_array[0][1] == counting_array[1][1]:
        print(counting_array[1][0])
    else:
        print(counting_array[0][0])
# print('counting_array',counting_array)
print(max(a)-min(a))