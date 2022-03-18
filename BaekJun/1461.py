import sys
sys.stdin = open("input.text","r")
import sys
N,M = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))

A = sorted(A)
B=[]
C=[]
BB=[]
CC=[]
cnt = 0
maxValue = 0
for i in A:
    if i>0:
        B.append(i)
    else:
        C.append(i)
B.reverse()
for i in B:
    cnt +=1
    if cnt%M==1:
        BB.append(i)
cnt = 0
for i in C:
    cnt +=1
    if cnt%M==1:
        CC.append(i)

if len(BB)>0 and len(CC)>0:
    maxValue = max(BB[0],-CC[0])
elif len(BB)==0:
    maxValue = -CC[0]
else:
    maxValue = BB[0]
print(sum(BB)*2-sum(CC)*2-maxValue)
