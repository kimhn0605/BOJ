# 1296 : 팀 이름 정하기

name = input()          # name : 연두 이름 
n = int(input())        # n : 팀 이름 후보의 개수 

result_li = []
team_li = []    

for _ in range(n) :     # 팀 후보 입력받아서 team_li 에 저장
  team_li.append(input())
  
team_li.sort()          # 확률 높은 팀이 여럿 있을 때, 사전 순으로 앞서는 팀을 출력하기 위해 정렬

for team in team_li :   # 팀 하나씩 순회하면서 L, O, V, E 개수 저장
  L = name.count('L') + team.count('L') 
  O = name.count('O') + team.count('O')
  V = name.count('V') + team.count('V')
  E = name.count('E') + team.count('E')
  
  result = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100      # result 에 연산 결과 저장
  result_li.append(result)        # result_li 에 팀별 연산 결과 저장

# 가장 높은 확률의 인덱스를 구해서 team_li 에 대입
print(team_li[result_li.index(max(result_li))])
