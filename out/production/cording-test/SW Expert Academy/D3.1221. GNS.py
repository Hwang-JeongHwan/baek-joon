num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for _ in range(int(input())):
    
    tc, length = input().split()
    data = list(input().split())
    result = []
    for i in data:
        result.append(num.index(i))
    #print(result)
    #print(result)
    result.sort()
    print('{}'.format(tc))
    # print(result)
    for j in result:
        print(num[j],end=' ')

