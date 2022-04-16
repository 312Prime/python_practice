import sys
sys.stdin = open("input.text","r")

N = list(map(int,sys.stdin.readline()))
isN0 = N.count(0)!=0
isN3 = sum(N)%3==0

if isN0&isN3:
    N=sorted(N)
    N.reverse()
    result=''.join(map(str,N))
    print(result)
else:
    print(-1)
    
    
    