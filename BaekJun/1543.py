import sys
sys.stdin = open("input.text","r")

n=input()
s=input()
count = 0

while True:
    if  n.find(s)==-1:
        break
    if n.find(s)!=-1:
        n=n[n.find(s)+len(s):]
        count+=1
print(count)