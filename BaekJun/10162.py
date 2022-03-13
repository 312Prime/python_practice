import sys
sys.stdin = open("input.text","r")

n= int(input())
countA = 0
countB = 0
countC = 0

while n>0:
    if n%10!=0:
        countA = -1
        countB = -1
        countC = -1
        break
    if n>=300:
        countA += n//300
        n = n%300
        continue
    if n>=60:
        countB += n//60
        n = n%60
        continue
    if n>=10:
        countC += n//10
        n = n%10
        continue
if countA== -1:
    print(-1)
else:
    print(countA, countB, countC)

