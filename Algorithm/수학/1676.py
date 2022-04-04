# 1676 : 팩토리얼 0의 개수

n = int(input())      # n 입력받기
factorial = 1         
count = 0             # 0 의 개수 셀 변수 count 선언

# n 의 팩토리얼 구하기
for i in range(2, n+1) :    
  factorial *= i

factorial = str(factorial)    # 문자열 형태로 변환

i = -1      # 문자의 뒤에서부터 검사하기 위해 -1 로 설정
while (factorial[i] == '0') :   # 뒤에서부터 시작해서 0 이 나올 때까지만 반복
  count += 1
  i -= 1
  
print(count)