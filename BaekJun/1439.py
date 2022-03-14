import sys
sys.stdin = open("input.text","r")

n=list(map(int,input()))
now = -1
a=[]
for i in n:
    if i!=now:
        a.append(i)
        now = i
print(len(a)//2)