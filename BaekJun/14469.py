import sys
sys.stdin = open("input.text","r")

n = int(sys.stdin.readline())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
A = sorted(A)
cnt = 0
extra = 0

for i in A:
    extra = 0
    if i[0]<cnt:
        extra = cnt-i[0]

    cnt = i[0]+i[1]+extra
print(cnt)