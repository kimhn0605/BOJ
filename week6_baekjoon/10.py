t = int(input())

for i in range(1, t+1):
    print(' '*(t-i) + '*'*i)
    # (t-i)만큼 띄어쓰기한 후 * 출력