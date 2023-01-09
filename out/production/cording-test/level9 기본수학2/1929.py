import math
def isPrime(num):
    if num == 1:
        return False
    sqr=int(math.sqrt(num))
    for i in range(2,sqr+1):
        if(num%i == 0):
            return False
    return True





M,N = map(int,input().split())


for i in range(M,N+1):
    
    if isPrime(i) == True:
        print(i)
