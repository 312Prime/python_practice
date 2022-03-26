import sys
sys.stdin = open("input.text","r")

def changeNum(a) :
    if a == 1:
        a = 0
    else:
        a = 1

N,M = map(int,input().split())
A = [list(map(int,input())) for _ in range(N)]
B = [list(map(int,input())) for _ in range(N)]
C = A
cnt = 0

for i in range(N):
    for j in range(M):
        if A[i][j] == B[i][j]:
            C[i][j] = 0
        else:
            C[i][j] = 1
print(C)
