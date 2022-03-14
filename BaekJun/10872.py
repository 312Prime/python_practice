import sys
sys.stdin = open("input.text","r")

N = int(input())
count = 1

for i in range(N):
    count = count*(i+1)
print(count)