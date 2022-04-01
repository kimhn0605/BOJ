# 10814 : 나이순 정렬

n = int(input())      # n 입력받기
members = []          # 빈 리스트 선언

for _ in range(n) :
  age, name = map(str, input().split())        # 나이, 이름 입력받기
  members.append((int(age), name))             # (나이, 이름) 을 묶어서 리스트에 저장

members.sort(key = lambda x : x[0])            # 리스트의 첫 번째 요소인 `나이` 로 정렬해서 기존 배열 변환

for i in members :
  print(i[0], i[1])    # 정렬한 순서대로 나이, 이름 출력

# 나이순으로 정렬한 후 가입한 순서대로는 정렬을 따로 하지 않은 이유
# 파이썬은 기본적으로 stable 정렬이기 때문

# stable 정렬 (안정 정렬) 이란?
#  -> 입력 받은 값들 중에서 동일한 값이 있는 경우 해당 값의 순서를 그대로 유지
# ex) [1, 2, 3(x), 4, 5, 3(y)] 오름차순 정렬 
#  -> [1, 2, 3(x), 3(y), 4, 5] => x, y 앞뒤 순서 유지