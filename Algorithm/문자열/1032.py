# 1032 : 명령 프롬프트

# 방법 1)
n = int(input())                    # n 입력받기
li = []

for _ in range(n) :
  li.append(input())                # n 개의 단어 입력받기
  
result = li[0]                      # 입력받은 첫 번째 단어를 기준으로 설정

for word in li[1:] :                # 두 번째 단어부터 끝까지 순회
  for i in range(len(word)) :       # 단어의 길이만큼 순회
    if result[i] != word[i] :       # 인덱스로 알파벳 비교해서 다르면 ? 삽입
      result = result[:i] + "?" + result[i+1:]
      
print(result)

# 방법 2)
n = int(input())                    # n 입력받기

front = list(input())               # 처음 입력받은 단어만 따로 리스트에 저장
length = len(front)                 # length : 단어의 길이 저장

for i in range(n-1) :               # 나머지 단어의 입력이 들어올 때마다
  back = list(input())
  
  for j in range(length) :          # 단어의 길이만큼 순회하면서 알파벳 비교
    if front[j] != back[j] :
      front[j] = "?"

# print(front)
print("".join(front))               # join() : 문자열 합치는 메서드

# ex) abc / bac / cbc

# print(front) => ['?', '?', 'c']
# print("".join(front)) => ??c