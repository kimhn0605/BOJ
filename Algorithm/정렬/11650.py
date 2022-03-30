# 11650 : 좌표 정렬하기

n = int(input())          # n 입력받기
li = []                   # 빈 리스트 생성

for i in range(n) :
  x, y = map(int, input().split())      # x, y 입력받기
  li.append([x, y])                     # [x, y] 를 li 에 저장 -> 2차원 배열
  
li.sort()      # x, y 차례대로 정렬

for i in range(n) :
  print(li[i][0], li[i][1])     # 정렬 후 x, y 값 순서대로 출력