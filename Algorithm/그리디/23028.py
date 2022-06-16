# 23028 : 5학년은 다니기 싫어요

n, a, b = map(int, input().split())         # n : 끝낸 학기수, a : 이수한 전공 학점, b : 이수한 총 학점
x_li = [] 
y_li = []

for _ in range(10) :
  x, y = map(int, input().split())          # 학기별 전공/비전공 과목 개수 입력받기
  x_li.append(x)                            # x_li : 전공 과목 개수 담은 리스트
  y_li.append(y)                            # y_li : 비전공 과목 개수 담은 리스트

i = 0      # 인덱스

while (True) :
  
  n += 1                         # 현재 학기 갱신
  if n > 8 :                     # 8학기를 초과했다면
    print("Nae ga wae")          # 문구 출력 후 while문 탈출
    break
    
  # 한 학기에 최대 6과목만 이수 가능
  temp = x_li[i] + y_li[i] - 6
  
  if temp > 0 :                   # 7과목 이상으로 개설됐다면
    b += 18                               # 총 학점 : 현재 총 학점 + (학기당 최대 학점 18학점)
    
    if x_li[i] > 6 :                           # 전공 과목이 6과목보다 많이 개설됐다면
      a += (x_li[i] - (x_li[i]-6)) * 3         # 6과목에서 뺀 개수만큼만 누적해서 갱신
      
    else :                                # 전공 과목이 6과목 이하로 개설됐다면
      a += (x_li[i]) * 3                       # 열리는 전공 과목 개수 그대로 누적해서 갱신
      
  else :                          # 6과목 이하로 개설됐다면
    a += (x_li[i]) * 3                    # 열리는 전공 과목 개수 그대로 누적해서 갱신
    b += (x_li[i] + y_li[i]) * 3          # 총 학점 갱신
    
  if a >= 66 and b >= 130 :               # 전공 학점이 66 학점 이상이고, 총 학점이 130 학점 이상이라면
    print("Nice")                         # 문구 출력 후 while문 탈출
    break
  
  i += 1      # 인덱스 갱신