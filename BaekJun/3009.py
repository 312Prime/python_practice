import sys
sys.stdin = open("input.text","r")

A=[]
B=[]
for i in range(3):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
A.sort()
B.sort()
if A[0]==A[1]:
    c= A[2]
else:
    c= A[0]
if B[0]==B[1]:
    d= B[2]
else:
    d= B[0]
print(c,d)

    