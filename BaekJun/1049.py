import sys
sys.stdin = open("input.text","r")

N,M = map(int,input().split())
A=[list(map(int,input().split())) for _ in range(M)]
minSet = 9999999
minVal = 9999999

for i in range(M):
    if minSet>A[i][0]:
        minSet = A[i][0]
    if minVal>A[i][1]:
        minVal = A[i][1]
if (minSet>=minVal*6):
    print(N*minVal)
else:
    setVal1 = (N%6*minVal)+(N//6*minSet)
    setVal2 = (N//6+1)*minSet
    print(min(setVal1,setVal2))