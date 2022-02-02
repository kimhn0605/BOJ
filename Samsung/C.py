# 14888 : 연산자 끼워넣기

from itertools import permutations  # 순열 함수 (연산자 순서 의미 O)
import sys  
input = sys.stdin.readline 
n = int(input())
arr = list(map(int, input().split()))
plus, minus, multi, divide = map(int, input().split())

# 각 연산자 개수만큼 해당 숫자를 곱해서 리스트에 삽입
operation_list = []
operation_list += [1] * plus
operation_list += [2] * minus
operation_list += [3] * multi
operation_list += [4] * divide
#print(operation_list)

# 중복되지 않게 연산자 셋을 종류별로 만들어줌
operation_set = []
for numbers in list(permutations(operation_list)) :
  operation_set.append(numbers)
operation_set = list(set(operation_set))  # set() -> 중복 제거
#print(operation_set)
# 중복 제거하는 이유 : 같은 연산자가 존재할 때 다른 연산자로 보지 않기 때문. ex) + 연산자만 4개 있을 때

# 문제에 나온 최댓값/최솟값 조건
max_answer = -1000000001
min_answer = 1000000001

# +, -, *, / 가 나올 경우를 각각 조건에 맞게 써줌
for case in operation_set :
  answer = arr[0]  # 처음 입력한 숫자값 저장
  
  for i in range(n-1) :  # n이 아니라 n-1인 것 주의 ex) n=5 일 때 연산자는 4개여야 하니까 i=0~3 (4개)
    if case[i] == 1 :
      answer += arr[i+1]  # 연산자가 + 일 때
    elif case[i] == 2 :
      answer -= arr[i+1]
    elif case[i] == 3 :
      answer *= arr[i+1]
    elif case[i] == 4 :  # 나눗셈은 문제의 조건에 맞게 추가 조건이 따로 붙음.
      if answer < 0 :  # 이전 결과가 음수라면 양수로 바꾼 후 몫 구하고나서 다시 음수로 바꿔주기
       answer = -(-answer // arr[i+1])  # 정수값 몫만 구하는 거니까 연산자 기호는 //
      else :
        answer //= arr[i+1]

  # 최댓값/최솟값일 경우
  if answer < min_answer :
    min_answer = answer
  if answer > max_answer :  # 여기서 if 가 아니라 elif 로 쓰면 틀렸다고 나오는데 아직 이유를 못 찾음
    max_answer = answer

print(max_answer)
print(min_answer)

