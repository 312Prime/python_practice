import sys
sys.stdin = open("input.text","r")

n=int(sys.stdin.readline())
A=[0,1]

for i in range(n):
    A.append(A[i]+A[i+1])
print(A[n])