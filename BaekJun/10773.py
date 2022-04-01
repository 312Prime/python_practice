import sys
sys.stdin = open("input.text","r")

N = int(sys.stdin.readline())
A = []
val = 0

for i in range(N):
    val = int(sys.stdin.readline())
    if val == 0:
        A.pop(len(A)-1)
    else:
        A.append(val)
print(sum(A))