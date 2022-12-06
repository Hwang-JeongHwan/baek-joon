# 다이나믹 프로그래밍의 사용 조건을 만족하는지 확인
# 1. 최적부분 구조: 큰문제를 작은 문제로 나눌수 있습니다
# => f(4)를 구하고자할때 f(3) + f(2)임 => 큰문제를 해결하기 위해 작은문제 두개를 해결한
# 결과값을 가지고 있으면됨 
# 이처럼 작은 문제를 모아서 큰 문제를 해결할수있다는 점에서 최적 부분구조임

# 2. 중복되는 부분 문제 : 동일한 작은 문제를 반복적으로 해결합니다
# => f(4)를 구할때에도 f(2)가 2번 호출되는것을 볼수있음
# => 큰문제가 해결되는 과정에서 동일한 작은문제가 해결될수 있도록 요구되기때문에
# 중복되는 부분문제를 가진다고 표현할수 있음 
# 피보나치 수열은 다이나믹 프로그래밍의 사용조건을 만족함 

# 메모이제이션 : 탑다운 방식(하향식) 에서 사용됨 
# 메모이제이션은 다이나믹 프로그래밍을 구현하는 방법중 하나임
# 한번 계산한 결과를 메모리 공간에 메모하는 기법
# 같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져옴
# 값을 기록해 놓는다는 점에서 캐싱이라고도 함
# dp or d라고 배열의 이름을 설정

# 탑다운 vs 보텀업

# 탑다운 (메모이제이션) 방식은 하향식이라고도 하며 보텀업 방식은 상향식이라고도 함
# 탑다운 방식은 구현과정에서 재귀함수를 이용 -> 즉 큰문제를 해결하기 위해 
# 작은 문제들을 재귀적으로 호출하여 작은 문제들을 다 해결했을때 큰문제도 해결되도록
# 코드를 작성함
# 그러한 과정에서 한번 계산된 결과값을 기록하기 위해 메모이제이션 방식을 이용함

# 보텀업 방식은 아래쪽에서부터 작은문제를 하나씩 해결해 나가면서 먼저 계산한 문제들의
# 값을 활용해서 그다음 문제까지 차례대로 해결하나가는 방식이 특정임 -> 반복문 이용


# 다이나믹 프로그래밍의 전형적인 형태는 보텀업 방식임
# 결과 저장용 리스트는 DP 테이블이라고 부름

# 엄밀히 말하면 메모에제이션은 이전에 계산된 결과를 일시적으로 기록해 놓는 넓은
# 개념을 의미함
# 따라서 메모이제이션은 다이나믹 프로그래밍에 국한된 개념은 아님
# 한번 계산된 결과를 담아놓기만 하고 다이나믹 프로그래밍을 위해 횔용하지 않은수도 있음
