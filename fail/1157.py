# 1157 : 단어 공부 -> 코드 안 보고 혼자 다시 풀어보기

word = input().upper()  # 대소문자 구별 안한다고 했으니까 모두 대문자로 변경
word_point = list(set(word))  # 중복 문자 제거 후 리스트로 변환
count_li = []

for i in word_point : 
  count = word.count(i)  # count 를 통해 각 문자별 개수 세기
  count_li.append(count)
if count_li.count(max(count_li)) > 1 :  # 최대 개수 겹칠 때 물음표 출력
  print("?")
else :
  max_index = count_li.index(max(count_li))
  print(word_point[max_index])
