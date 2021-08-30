# 2839 : 설탕 배달 *** 해결 x

while True :
  n = int(input("킬로그램 수 : "))
  k5 = int(n / 5)   
  k3 = int((n - 5*k5) / 3)  

  if n % 5 == 0 :
    print(n / 5)
  elif (3*k3 + 5*k5) == n :
    print(k3 + k5)
  elif (3*k3 + 5*k5) != n :
    if k5 <= 2 :
      if (n-5*(k5-1)) % 3 == 0 :
        print( (n-5*(k5-1)) / 3 + k5-1)
      # else : 3으로도 안나눠떨어질 때
          #수행문장
      for i in range(1, k5) :
        if (n-5*(k5-i)) % 3 == 0 :
          print( (n-5*(k5-i)) / 3 + k5-i)
 
  else :
    print("-1")

  # 1) 5로 다 나눠지는지 확인
  # 2) 5로 최대한 나눠보고 3의 배수를 늘려감
  # 3) 3으로만 다 나눠지는지 확인
  # 4) 그래도 안되면 -1 출력