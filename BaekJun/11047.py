import sys
sys.stdin = open("input.text","r")

N,K= map(int,input().split())
moneyList=[]
count=0

for i in range(N):
    s= int(input())
    moneyList.append(s)
moneyList.sort(reverse=True)
for i in moneyList:
    if K>=i:
        count+=K//i
        K=K%i
print(count)