import sys
sys.stdin = open("input.text","r")

N = int(input())
A = [0,1]
C = []

for i in range(100):
    A.append(A[i]+A[i+1])

for i in range(N):
    C=[]
    a = int(input())
    while True:
        if a == 0:
            break
        for i in A:
            if a<i:
                a-=cnt
                C.append(cnt)
                break
            cnt = i
    C.sort()
    for i in C:
        print(i, end=' ')
    print()