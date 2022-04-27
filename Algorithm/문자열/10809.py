# 10809 : 알파벳 찾기

s = input()       # 문자열 입력받기

for i in range(97, 123) :                   # 아스키코드 => a : 97, z : 122
  if chr(i) in s :                          # 아스키코드를 문자로 변환했을 때 s 에 포함되어 있다면
    print(s.index(chr(i)), end = " ")       # 위치 출력
  else :                                    # s 에 포함되어 있지 않다면
    print(-1, end = " ")                    # -1 출력
    
