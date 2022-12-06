def solution(s):
    length = len(s)
    result = int(1e9)
    for i in range(1, length + 1):
        count = 1
        index = 0
        x = ''
        for j in range(i , length + 1, i):
           # print(s[index: j],s[j: i + j])
            if s[index: j]  == s[j : i + j]:
                
                count += 1
          #      print(count)
            else:
                if count > 1:
                    x += str(count) + s[index : j]
         #           print(x)
                    count = 1
                else:
                    x += s[index:j]
            index += i
        if j < length:
            x += s[j:]
        #print('x', x)
            
        
        result = min(result, len(x))
    
    return result
            
        
s = "xababcdcdababcdcd"
print(solution(s))