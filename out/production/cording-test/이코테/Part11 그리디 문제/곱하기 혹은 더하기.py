s = input()

result = 1
for i in s:
    
    if int(i) == 0:
        continue
    
    result *= int(i)
    
print(result)
# 이렇게 되면 1 1 이렇게 들어올때 곱해버림;;
