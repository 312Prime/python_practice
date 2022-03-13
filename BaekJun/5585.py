import sys
sys.stdin = open("input.text","r")

n=int(input())
count=0
n=1000-n
while n>0:
    if n>=500:
        count+=n//500
        n=n%500
        continue
    if n>=100:
        count+=n//100
        n=n%100
        continue
    if n>=50:
        count+=n//50
        n=n%50
        continue
    if n>=10:
        count+=n//10
        n=n%10
        continue
    if n>=5:
        count+=n//5
        n=n%5
        continue
    if n>=1:
        count+=n
        n=0
        continue
print(count)
