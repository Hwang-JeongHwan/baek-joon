T = int(input())
for i in range(T):
    D = input()
    a = []
    ans = 'YES'
    for j in D:
        if j == '(': #j가 '('이면 스택에 append
            a.append(j)
        else : #j가 '('가 아닌경우
            if len(a) > 0 : #스택의 길이가 0보다 크면
                a.pop() #스택의 제일위에서 pop
            else: ans = 'NO' 
            #j가 '('가 아니고 스택의 길이가 
            # 0보다 같거나 보다 작은경우
    if len(a) > 0 : #스택의 길이가 0보다 클경우 -> '(' 만 남은경우
        ans = 'NO'
    print(ans)        

 
