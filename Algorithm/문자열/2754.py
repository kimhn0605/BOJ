# 2754 : 학점계산

word = input()          # 학점 입력받기
alpha = word[0]         # alpha : 알파벳
grade = 0.0             # 평점은 F (0.0) 로 초기화

if alpha != 'F' :       # alpha 가 F 아닐 때
  op = word[1]          # op : +, 0, - 중 하나
  
  if alpha == 'A' :
    grade = 4.0
  elif alpha == 'B' :
    grade = 3.0
  elif alpha == 'C' :
    grade = 2.0
  elif alpha == 'D' :
    grade = 1.0
  else :
    grade = 0.0
    
  if op == '+' :
    grade += 0.3
  elif op == '-' :
    grade -= 0.3

print(grade)        