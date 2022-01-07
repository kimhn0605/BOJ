n, x = map(int, input().split())
li = list(map(int, input().split()))

for i in range(n):
    if(x > li[i]):
        print(li[i], end=' ')  # 출력 사이에 한 칸씩 공백 주기
        # end = '' : 빈 문자열 지정하면 다음 번 출력이 바로 뒤에 옴.
        