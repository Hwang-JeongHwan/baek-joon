dic = {'ZRO' : 0, 'ONE' : 1, 'TWO' : 2, 'THR' : 3, 'FOR' : 4, 'FIV' : 5
,'SIX' : 6, 'SVN' : 7, 'EGT' : 8, 'NIN' : 9}
dic2 = {0 : 'ZRO' , 1 : 'ONE' , 2 : 'TWO', 3 : 'THR', 4 : 'FOR', 5 : 'FIV'
,6 : 'SIX', 7 : 'SVN', 8 : 'EGT', 9 : 'NIN'}


tc = int(input())

for t in range(tc):
    n, length = input().split()
    length = int(length)
    s = input().split()
    result = []
    for i in range(length):
        if s[i] in dic:
            # print(dic[s[i]])
            result.append(dic[s[i]])
    
    result.sort()
    
    for i in range(len(result)):
        result[i] = dic2[result[i]]
    print('{}'.format(n), end=' ')
    print(*result, end=' ')
    print()