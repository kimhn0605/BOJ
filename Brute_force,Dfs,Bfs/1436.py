# 1436 : 영화감독 숌

n = int(input())  
count = 0  # 666이 들어갈 때마다 카운트 1씩 증가
result = 666  # 첫 번째 종말 숫자

while n != count :
  if '666' in str(result) :
    count += 1
  result += 1
print(result-1)  # n == count 인 순간에는 이미 result += 1 이 적용됐으니까 -1 해줌