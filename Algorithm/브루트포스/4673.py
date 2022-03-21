# 4673 : 셀프 넘버

li = set()                           # 생성자 담을 집합 
numbers = list(range(1, 10001))      # numbers : 1 ~ 10000 숫자가 담긴 리스트

for num in numbers :                 # numbers 에 담겨있는 숫자들을 하나씩 돌아가면서
  for i in str(num) :                # 각 자리수를 더하기 위해 문자형으로 변환하여
    num += int(i)                    # 기존 num 에 각 자리수를 차례대로 더해줌
  if num <= 10000 :                  # 다 더한 후 n 값이 10000 이하라면
    li.add(num)                      # 생성자 집합에 원소 추가
    
numbers = set(numbers)               # set 의 차집합 연산을 위해 set 자료형으로 변환
result = numbers - li                # set 의 차집합 연산자 (-) 사용

for n in sorted(result) :            # result 정렬 후 하나씩 출력
  print(n)