# 1032 : 명령 프롬프트

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