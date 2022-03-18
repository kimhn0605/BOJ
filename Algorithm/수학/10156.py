# 과자

k, n, m = map(int, input().split())
result = k * n - m

if result <= 0 :      # 받아야 할 돈이 음수라면
  print(0)            # 0원 출력
else : 
  print(result)