import sys
sys.stdin = open("input.text","r")

T = int(sys.stdin.readline())
n = 0
countQ = 0
countD = 0
countN = 0
countP = 0
for i in range(T):
    countQ = 0
    countD = 0
    countN = 0
    countP = 0
    n = int(sys.stdin.readline())
    while True:
        if n == 0:
            print(countQ , countD , countN, countP)
            break
        if n >= 25:
            countQ = n//25
            n = n%25
            continue
        if n >= 10:
            countD = n//10
            n = n%10
            continue
        if n >= 5:
            countN = n//5
            n = n%5
            continue
        if n >= 1:
            countP = n
            n = 0
            continue

        
            




