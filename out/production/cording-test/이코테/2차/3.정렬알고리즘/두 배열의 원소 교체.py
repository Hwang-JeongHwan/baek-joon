# k번 바꿔치기 , 
# 모든 원소의 합이 최대가 되도록 해야함 
# a에서 제일작은거 3개랑 b에서 제일큰거 3개를 바꿔줌

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse = True)
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))