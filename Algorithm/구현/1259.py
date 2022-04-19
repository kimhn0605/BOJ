# 1259 : 팰린드롬수

while (True) :
  count = 0
  word = input()          # 수 입력받기
  
  if word == '0' :        # 0 을 입력받으면 종료
    break
    
  li_start = word[::]     # li_start : 앞에서부터 읽은 순서
  li_end = word[::-1]     # li_end : 뒤에서부터 읽은 순서

  for i in range(len(word)) :
    if li_start[i] == li_end[i] :     # li_start 와 li_end 비교해서 일치할 때마다 count + 1
      count += 1
      
  if count == len(word) :             # count 개수와 입력받은 숫자의 길이가 같다면
    print("yes")                      # yes 출력
  else :          
    print("no")