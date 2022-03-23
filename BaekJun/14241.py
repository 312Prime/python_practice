import sys
sys.stdin = open("input.text","r")

n = int(input())
A = list(map(int,input().split()))

score = 0
now = 0

A = sorted(A)
while True:
    now = 0
    if len(A) ==1:
        break
    score += A[0]*A[1]
    now = A.pop(0)+A.pop(0)
    A.append(now)
print(score)