N = int(5)
A = (20, 10, 35, 30, 7)
M=A[0]
m =A[0]
for i in range(N):
    if A[i]>M:
        M= A[i]
    elif A[i]<m:
        m= A[i]
print(M,m)