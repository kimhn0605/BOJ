# 18352 : 특정 거리의 도시 찾기

# 도로의 거리가 모두 1 이니까 BFS 사용

import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())       # n, m, k, x 입력받기
graph = [[] for _ in range(n+1)]                          
dist = [-1 for _ in range(n+1)]                           # 거리 갱신 (-1 이면 아직 방문하지 않은 상태)

q = deque([x])            # 시작점인 x 는 초깃값
dist[x] = 0               # 현재 시작점은 0 으로 초기화
flag = True               # 최단 거리가 k 인 도시가 존재하지 않을 때 판별 유무

for _ in range(m) :
  a, b = map(int, sys.stdin.readline().split())           # 인덱스별로 가리키고 있는 노드 저장 
  graph[a].append(b)                                      # ex) [ [], [2, 3], [3, 4], [], [] ]
  
# BFS 구현
while q : 
  now = q.popleft()             
  for next in graph[now] :
    if dist[next] == -1 :             # 아직 방문하지 않은 노드라면
      dist[next] = dist[now] + 1      # 현재 노드에서 +1 해줌으로써 거리 갱신
      q.append(next)

for i in range(n+1) :
  if dist[i] == k :                   #  최단 거리가 k 인 경우 출력하고 flag 값 False 로 변경
    print(i)
    flag = False
    
if flag :                             # flag 값이 그대로 True 라면 -1 반환
  print(-1)     