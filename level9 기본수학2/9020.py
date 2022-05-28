# def isPrime(n):                         # 소수인지 확인하는 함수
# 	if n < 2:                           # 매개변수가 2이하이면 소수 아님
# 		return False                    # False 반환
# 	for i in range(2,int(n**0.5)+1):    # 매개변수의 제곱근까지 돌면서 나눠어 떨어지는 확인
# 		if n % i == 0:                  # 만약 나눠 떨어지면 소수 아님
# 			return False                # False 반환
# 	return True                         # 다 패스했으면 소수~

# test_case = int(input())                # 테스터케이스 입력받기 

# for _ in range(test_case):                         # 케이스만큼만 도는 반복문
# 	input_number = int(input())                    # 수 입력받기
# 	for i in range(input_number//2, 1, -1):  # 입력받은 수의 절반부터 역순으로 체크(이유)
#                                              #(이유) 소수의 차이가 작은거부터 출력하기 위해
# 		if isPrime(i) and isPrime(input_number-i): # 만약 i와 입력 받은 수 - i가 소수면 출력
# 			print(i, input_number-i)               # 출력
# 			break                                  # 출력했음 탈출 (안하면 다음 나옴)





def primeList(num):
	check = [False,False]+[True]*(num-2) #체크리스트 배열 만들어줌
	# 0 ,1 을제외한 num까지의 인덱스를 모두 True로 만듬
	for i in range(num):
		if check[i] == True: #check[i]번째 원소가 True면
			for j in range(2*i,num,i):
				
				check[j]=False #check[i배 한수]를 전부 false로
	return check # 이렇게 되면 각 인덱스별로 소수인지 아닌지 True false가 저장된 배열이 반환됨



T = int(input())

for i in range(T):
	N = int(input())
	check = primeList(N)
	a = N//2
	b = a 
	for j in range(N):
		print(j)
		if check[a] == True and check[b] == True:
			print(a,b)
			break
		a-=1
		b+=1


