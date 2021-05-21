T = int(input())

for i in range(0, T):

    a, b = map(int, input().split(' '))
    # split() = split(' ')
    # split('') -> 오류

    print(a + b)