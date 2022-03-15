import sys
sys.stdin = open("input.text","r")
import sys
import heapq
N = int(sys.stdin.readline())
numList = []
for i in range(N):
    numList.append(int(sys.stdin.readline()))
heapq.heapify(numList)
if len(numList) == 1:
    print(0)
else:
    count = 0
    while len(numList)>1:
        a = heapq.heappop(numList)
        b = heapq.heappop(numList)
        heapq.heappush(numList,a+b)
        count += a+b
    print(count)