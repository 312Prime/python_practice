import sys
sys.stdin = open("input.text","r")

n = int(input())
A = list(map(int,input().split()))

print(sum(A)-max(A))