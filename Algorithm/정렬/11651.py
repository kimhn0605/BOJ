# 11651 : 좌표 정렬하기 2

n = int(input())        # n 입력받기
xy_li = []              # (x, y) 쌍을 담을 리스트 선언

for _ in range(n) :     
  x, y = map(int, input().split())      # x, y 입력받기
  xy_li.append([y, x])                  # y 좌표부터 정렬해야 하니까 (y, x) 쌍으로 리스트에 저장

xy_li.sort()            # y 좌표 정렬 후 x 좌표 정렬

for i in range(len(xy_li)) :    
  print(xy_li[i][1], xy_li[i][0])