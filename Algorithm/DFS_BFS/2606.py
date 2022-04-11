# 2606 : 바이러스

# DFS 방법 사용

n = int(input())          # n : 컴퓨터 개수  
line = int(input())       # line : 간선 개수 (= 쌍 개수)

graph = [[] * n for _ in range(n+1)]      # 2차원 배열 => n+1 한 이유는 편의상 인덱스 번호 맞추기 위해 (1 ~ 7)

for _ in range(line) :
  i, j = map(int, input().split())        # 연결할 노드 (i) 와 연결받을 노드 (v) 입력받기
  
  # 무방향 그래프이기 때문에 양방향으로 움직일 수 있도록 양쪽 배열에 모두 추가
  graph[i].append(j)
  graph[j].append(i)

# print("최종", graph)                # 아래 예시 참고
count = 0                             # 1번 컴퓨터를 통해 바이러스에 걸린 컴퓨터 수
visited = []                          # 방문 처리할 배열

def dfs(graph, start, visited) :
  global count                        # 함수 내/외부에서도 count 값이 누적되도록
  visited.append(start)               # visited 배열에 현재 노드 추가 => 방문 처리
  # print("visit", visited)           # 아래 예시 참고
  
  for node in graph[start] :          # 현재 노드와 연결된 노드들을 하나씩 순회
    if node not in visited :          # 해당 노드가 visited 배열에 없다면   
      count += 1                      # 카운트 세주고 재귀 호출
      dfs(graph, node, visited)        
      
  return count

print(dfs(graph, 1, visited))         # DFS 시작점 : 1번 노드

## 예시 
# 컴퓨터 개수 : 7, 간선 개수 : 6 일 때
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

## 최종 graph 배열
# 최종 [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
# 0 번 인덱스는 편의상 추가 => 그래서 graph 배열 초기화할 때 n 이 아닌 n + 1 라고 써준 것

## 방문되는 순서 (visited 배열 출력)
# visit [1]
# visit [1, 2]
# visit [1, 2, 3]
# visit [1, 2, 3, 5]
# visit [1, 2, 3, 5, 6]