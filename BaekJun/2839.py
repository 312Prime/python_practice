import sys
sys.stdin = open("input.text","r")

n=int(input())
count = 0

while n>0:
    if n%5 == 0:
        count += n//5
        break
    elif n<3:
        count = -1
        break
    else:
        n=n-3
        count+=1
        continue

print(count)