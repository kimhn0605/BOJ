# 1929 : 소수 구하기 
# --> 시간초과 오류 해결 x
# 참고 자료 : https://apape1225.tistory.com/37

m, n = map(int, input().split())
for i in range(m, n+1) :
  count = 0
  for k in range(2, i) :
    if i % k == 0 :
      count += 1  # 소수 아님
      break
  if count == 0 :
    print(i)


