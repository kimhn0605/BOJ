# 1065 : 한수

n = int(input())    # n 입력받기
count = 0           # 1 ~ n 사이의 한수 개수 (출력할 값)

if n < 100 :        # 만약 n 이 100 미만이라면
  count = n         # 한수 개수는 n 과 동일
else :              # 만약 n 이 100 이상이라면
  count = 99        # 1~99 까지는 무조건 한수이기 때문에 +99
  for i in range(100, n+1) :      # 100부터 n 까지 돌면서
    slicing = str(i)              # 각 자릿수를 비교하기 위해 문자열 형태로 변환
    if (int(slicing[0]) - int(slicing[1])) == (int(slicing[1]) - int(slicing[2])) :   # 한수 조건에 해당하면
      count += 1    # count + 1
      
print(count)