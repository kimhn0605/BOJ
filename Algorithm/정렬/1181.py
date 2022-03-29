# 1181 : 단어 정렬

# 방법 1 : 사전 순으로 정렬 후 길이 비교
import operator                 # 딕셔너리의 value값 기준으로 정렬하기 위해 operator 임포트

n = int(input())                # n 입력받기
li = {}                         # 딕셔너리형 변수 li 선언

for _ in range(n) :
  word = input()                # 입력받은 단어 word 변수에 저장
  li[word] = len(word)          # {단어 : 단어 길이} 형태로 딕셔너리에 저장

li = dict(sorted(li.items()))   # 우선 단어를 사전 순으로 먼저 정렬

# 단어를 사전 순으로 정렬한 이후에 길이 순으로 정렬
# operator.itemgetter(1) : 아이템의 1번째 인덱스, 즉 딕셔너리의 value 값을 정렬 기준으로 삼겠다는 의미
sorted_dict = dict(sorted(li.items(), key=operator.itemgetter(1)))

for i in sorted_dict.keys() :
  print(i)                      # 키 값만 출력

# 길이로 먼저 정렬하면 나중에 sorted() 사용 시 
# 길이 상관없이 사전 순으로 다시 정렬되기 때문에 사전 순서로 먼저 정렬

# 방법 2 : 길이 비교 후 사전 순으로 정렬
n = int(input())              # n 입력받기
li = {}                       # 딕셔너리형 변수 li 선언
result = []                   # 정렬된 원소 담을 result 리스트 선언

for _ in range(n) :     
  word = input()              # word : 입력받은 문자
  length = len(word)          # length : 입력받은 문자의 길이
  li[word] = length           # 입력받은 문자를 key로, 원소의 길이를 value 로 하여 딕셔너리에 저장
  
# sorted_word : value 를 기준으로 오름차순 정렬
sorted_word = sorted(li.items(), key=lambda item : item[1], reverse = False)

# range(n) 으로 하지 않은 이유 : 중복된 원소가 제거되어 처음의 n값과 다를 수 있기 때문
for i in range(len(sorted_word)) :
  result.append(sorted_word[i][0])      # key 만 따로 빼내어 result 리스트에 저장
  
i = 0 
while (i < len(result)-1) :
  count = 0         # 문자 길이가 같을 때마다 카운트 셀 변수
  
  while (True) :
    if i == len(result)-1 :     # 인덱스 i 가 맨 마지막 원소를 가리키고 있다면
      result[i-count:i+1] = sorted(result[i-count:i+1])        # 해당 부분을 정렬하고 break
      break
    elif len(result[i]) == len(result[i+1]) :        # 인덱스 i와 i+1 의 문자 길이가 같다면
      count += 1                                     # count + 1 해주고 다른 길이가 나타날 때까지 반복
      i += 1
    else :          # 인덱스 i와 i+1 의 문자 길이가 같지 않을 때
      if count > 0 :     # count 값이 0보다 크다면 (중복되는 길이가 존재한다면)
        # 누적된 count 값만큼 해당 리스트 부분 정렬하고 break
        result[i-count:i+1] = sorted(result[i-count:i+1])
        i += 1
        break
      else :           # count 값이 0이라면 (중복되는 길이가 존재하지 않다면)
        i += 1         # 인덱스만 +1
        
for i in range(len(result)) :
  print(result[i].replace('"',''))        # 문자열에서 따옴표 제거 후 하나씩 출력