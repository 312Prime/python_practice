import sys
sys.stdin = open("input.text","r")

R,C= map(int,input().split())
count = []
minValue = 1000
A = []
countLR = True
I=0
J=0

if R%2 == 1:
    for i in range(R):
        count.append("D")
        for i in range(C-1):
            if countLR == True:
                count.append("R")
            else :
                count.append("L")
        countLR = -countLR
    count = ''.join(str(s) for s in count)
    print(count[1:])
else:
    if C%2 == 1:
        for i in range(C):
            count.append("R")
            for i in range(R-1):
                if countLR == True:
                    count.append("D")
                else :
                    count.append("U")
            countLR = -countLR
        count = ''.join(str(s) for s in count)
        print(count[1:])
    else:
        A = [list(map(int,input().split())) for _ in range(R)]
        for i in range(R):
            if i%2 == 0:
                for j in range(C):
                    if j%2 == 1:
                        if minValue > A[i][j]:
                            minValue = min(A[i][j],minValue)
                            I=i
                            J=j
            else:
                for j in range(C):
                    if j%2 == 0:
                        if minValue > A[i][j]:
                            minValue = min(A[i][j],minValue)
                            I=i-1
                            J=j
        for i in range(I):
            count.append("D")
            for j in range(C-1):
                if countLR == True:
                    count.append("R")
                else:
                    count.append("L")
            countLR = -countLR
        if J%2==1:
            count.append("DD")
            for i in range((J-1)//2):
                count.append("RURD")
            count.append("R")
            for i in range(C//2-(J+1)//2):
                count.append("RURD")
            for i in range(R-I-2):
                count.append("D")
                for j in range(C-1):
                    if countLR == True:
                        count.append("L")
                    else:
                        count.append("R")
                countLR = -countLR
            count = ''.join(str(s) for s in count)
            print(count[1:])
        else:
            I=I+1
            count.append("D")
            for i in range(J//2):
                count.append("DRUR")
            count.append("R")
            for i in range(C//2-(J+3)//2):
                count.append("DRUR")
            count.append("D")
            for i in range(R-I-1):
                count.append("D")
                for j in range(C-1):
                    if countLR == True:
                        count.append("L")
                    else:
                        count.append("R")
                countLR = -countLR
            count = ''.join(str(s) for s in count)
            print(count[1:])