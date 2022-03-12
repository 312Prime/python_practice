import sys
sys.stdin = open("input.text","r")

n= int(input())
a= list(map(int,input().split()))
a= sorted(a)
now = 0
count = 0

for i in a:
    now += i
    count += now
print (count)