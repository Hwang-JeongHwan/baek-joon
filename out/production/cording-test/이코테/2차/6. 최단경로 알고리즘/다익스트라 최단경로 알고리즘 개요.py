# 특정한 노드에서 출발하여 다른 모든노드로 가는 최단 경로를 계산합니다.
# 다익스트라 최단 경로 알고리즘은 음의 간선이 없을 때 정상적으로 동작합니다.
# 현실 세계의 도로(간선)은 음의 간선으로 표현되지 않습니다.
# 다익스트라 최단 경로 알고리즘은 그리디 알고리즘으로 분류됩니다
# 매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정을 반복합니다. 

# 알고리즘의 동작과정
# 1. 출발 노드를 설정합니다
# 2. 최단 거리 테이블을 초기화 합니다, 초기에서 다른노드로 가는 모든 비용은 무한,
# 자기 자신으로 가는 비용은 0으로
# 3. 방문하지 않은 노드중에서 최단거리가 가장 짧은 노드를 선택합니다
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신합니다
# 5. 위 과정에서 3번과 4번을 반복합니다

# 알고리즘 동작 과정에서 최단 거리 테이블은 각 노드에 대한 현재까지의 최단 거리 정보를
# 가지고 있음

# 처리 과정에서 더 짧은 경로를 찾으면 '이제부터는 이 경로가 제일 짧은 경로야'라고
# 갱신함 


# 그리디 알고리즘: 매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택해
# 임의의 과정을 반복하므로 다익스트라 알고리즘은 그리디 알고리즘에 속함

# 단계를 거치며 한 번 처리된 노드의 최단 거리는 고정 되어 더 이상 바뀌지 않음
# 한 단계당 하나의노드에 대한 최단 거리를 확실히 찾는것으로 이해할 수 있음

# 다익스트라 알고리즘을 수행한 뒤에 테이블에 각 노드까지의 최단 거리 정보가 저장됨
# 완벽한 형태의 최단 경로를 구하려면 소스코드에 추가적인 기능을 넣어야함 

