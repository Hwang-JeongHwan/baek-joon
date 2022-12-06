
tc = int(input())

for t in range(1, tc + 1):
    n, m = map(int,input().split())
    data = []
    for _ in range(n):
        data.append(int(input()))
    
    start = 1 # 하한값은 1초
    end = max(data) * m # 제일 오래걸리는 입국심사대 * 사람수 = 상한값

    while start <= end:
        mid = (start + end) // 2
        count = 0
        for i in range(n):
            count += mid // data[i]
        
            if count >= m:
                result = mid
                end = mid - 1
                break
        if count < m:
            start = mid + 1

    print('#{} {}'.format(t, result))