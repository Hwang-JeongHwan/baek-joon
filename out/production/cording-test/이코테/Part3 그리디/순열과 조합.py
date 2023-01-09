# 모든 경우의 수를 고려해야 할 때 어떤 라이브러를 효과적으로 사용할수 있을까?

# 순열: 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는것
# {'A', 'B', 'C'}에서 세 개를 선택하여 나열하는 경우:'ABC','ACB','BAC','BCA','CAB','CBA'
# 순열의 수: nPr = n*(n - 1) * (n - 2)* ''' * (n - r + 1)
from itertools import permutations
data = ['A', 'B', 'C'] # 데이터 준비
result = list(permutations(data ,3)) # 모든 순열 구하기
print(result)

# 조합: 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것
# {'A', 'B', 'C'}에서 순서를 고려하지 않고 두개를 뽑는 경우: 'AB','AC','BC'
# 조합의 수 nCr = n*(n - 1) * (n - 2)* ''' * (n - r + 1) / r!

from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기
print(result)