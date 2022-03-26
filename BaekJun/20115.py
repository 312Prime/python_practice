import heapq
import sys
sys.stdin = open("input.text","r")

import heapq
import sys

n= int(sys.stdin.readline())
A = list(map(float,sys.stdin.readline().split()))
A.sort(reverse=True)
for i in range(0,n-1):
    if A[i] >= A[i+1]:
        cnt = A[i] + (A[i+1]/2)
        A[i+1] = cnt
    else:
        cnt = A[i+1] + (A[i]/2)
        A[i+1] = cnt
print((A[-1]))