import sys
sys.stdin = open("input.text","r")

n=int(input())
A=[]
now=0
count=0
var = 0

for i in range(n):
    A.append(int(input()))
A.reverse()
now=A[0]
A=A[1:]
for i in A:
    if now <= i:
        count+=A[var]-now+1
        A[var]= now-1
    now = A[var]
    var+=1 
print(count)