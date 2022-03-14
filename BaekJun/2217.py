import sys
sys.stdin = open("input.text","r")

N = int(input())
n=0
A=[]
B=[]
for i in range(N):
    A.append(int(input()))
A.sort(reverse=True)
for i in A:
    n+=1
    B.append(i*n)
print(max(B))
