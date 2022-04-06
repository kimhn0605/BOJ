# 1316 : 그룹 단어 체커

# 방법 1 
n = int(input())         # n 입력받기
group_word = 0           # 그룹 단어 개수 세는 변수

for _ in range(n):       # n 번만큼 반복
    word = input()       # 단어 입력받기
    error = 0            
    
    for index in range(len(word)-1):              # 인덱스 범위 생성 : 0 ~ 마지막 인덱스까지
        if word[index] != word[index+1]:          # 연속된 두 문자가 다르다면
            new_word = word[index+1:]             # 현재 글자 이후 문자열을 새로운 단어로 생성
            if new_word.count(word[index]) > 0:   # 뒤에 남아있는 문자열에서 현재 글자가 있있다면
                error += 1                        # error += 1
                
    if error == 0:          # error가 0 인 단어만
        group_word += 1     # 그룹 단어 개수 += 1
        
print(group_word)           # 그룹 단어 개수 출력

# 방법 2 
n = int(input())            # n 입력받기
group_word_count = 0        # 그룹 단어 개수 세는 변수

for _ in range(n) :         # n 번만큼 반복
  word = list(input())      # 단어 입력받기
  new = []                  # 연속된 문자를 하나의 문자로 압축하여 리스트에 새로 저장
  
  i = 0       
  j = 1
  
  if len(word) == 1 :       # 단어 길이가 한 자리라면
    new.append(word[0])     # new 에 바로 저장
 
  while (len(word) >= 2) :      # 단어 길이가 두 자리 이상일 때
    if word[i] == word[j] :     # 연속된 문자라면
      j += 1                    # 언제까지 연속되는지 확인하기 위해 j += 1
      if j == len(word) :       # 만약 j 가 인덱스 범위를 초과했다면
        new.append(word[i])     # 남겨져있는 i 를 new 에 저장하고 while 문 탈출
        break
    else :                      # 연속된 문자가 아니라면
      new.append(word[i])       # 비교했던 앞의 인덱스를 먼저 new 에 저장
      i = j                     # 연속되지 않은 문자 시작점을 다시 i 에 할당
      j = i + 1                 # 위 과정 반복
      if j == len(word) :       # 만약 j 가 인덱스 범위를 초과했다면
        new.append(word[i])     # 남겨져있는 i 를 new 에 저장하고 while 문 탈출
        break
  
  count = 0         # 입력 단어마다 count 값 초기화
  
  for i in range(len(new)) :    
    if new.count(new[i]) == 1 : # new 리스트에 자신의 원소와 중복되는 원소가 없다면 count += 1
      count += 1                
  if count == len(new) :        # count 값이 new 리스트 길이와 동일하다면 모두 유일한 값이라는 거니까
    group_word_count += 1       # 그룹 단어 개수 += 1
    
print(group_word_count)        # 그룹 단어 개수 출력

# 예시 : ccazzzzbb
# new : ['c', 'a', 'z', 'b']
# count : 4, len(new) : 4 => 그룹 단어 O

# 예시 : aabbbccb
# new : ['a', 'b', 'c', 'b']
# count : 2, len(new) : 4 => 그룹 단어 X