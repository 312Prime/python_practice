import sys
sys.stdin = open("input.text","r")

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
B = []
distance = 0
A = sorted(A)
A.reverse()
now = A[0]
for i in A[1:]:
    B.append(now-i)
    now = i
B = sorted(B)
B.reverse()
B=B[K-1:]
print(sum(B))