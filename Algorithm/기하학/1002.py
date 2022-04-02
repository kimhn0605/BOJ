# 1002 : 터렛

import math         # pow (제곱), sqrt (제곱근) 

n = int(input())    # n 입력받기

for _ in range(n) :
  x1, y1, r1, x2, y2, r2 = map(int, input().split())    # 좌표 입력받기

  # distance : 두 중심 (x1, y1), (x2, y2) 사이의 거리 (원의 방정식 활용)
  distance = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))
  
  count = 0   # 아래 조건문에 해당하지 않으면 0
  
  # 두 원이 완벽하게 일치하는 경우 -> 접점이 무한대니까 -1 반환
  if distance == 0 and r1 == r2 :      
    count = -1
  
  # 두 원이 내접하거나 외접할 때 -> 접점이 1개니까 1 반환
  elif abs(r1 - r2) == distance or r1 + r2 == distance :
    count = 1
    
  # 두 원이 서로 다른 두 점에서 만날 때 -> 점점이 2개니까 2 반환
  elif r1 + r2 > distance and abs(r1 - r2) < distance :
    count = 2
    
  print(count)
  
# 두 개의 원의 교점이 적의 위치를 의미
#  => 교점의 개수를 구하는 문제
