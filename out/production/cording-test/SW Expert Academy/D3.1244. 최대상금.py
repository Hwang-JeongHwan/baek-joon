t = int(input())

for i in range(1, t + 1):
    num, c = input().split()
    
    data = set([num]) # set(num)으로 선언시 {'1','2','3'} 이런식으로 들어감 
    data2 = set()
    for j in range(int(c)):
        while data:
            now = list(data.pop()) # 이렇게 하면 ['1','2','3']으로 리스트가 만들어짐
            for k in range(len(now)):
                for l in range(k + 1, len(now)): # 이렇게해야 같은걸 바꾸고 나서 집어넣는 일이 없음
                    # k 부터 하면 k = l 일때 쓸데없는 값이 들어가버림 
                    now[k],now[l] = now[l],now[k]
                    data2.add(''.join(now))
                    now[k],now[l] = now[l],now[k]
            
        data = data2
        data2 = set()
    
    print('#{} {}'.format(i, max(data)))


