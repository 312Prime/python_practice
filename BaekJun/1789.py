import sys
sys.stdin = open("input.text","r")

S = int(input())
N=0
count = 0
while True:
    if S>=N:
        count+=1
        N=N+count
        continue
    if S<N:
        break
print(count-1)