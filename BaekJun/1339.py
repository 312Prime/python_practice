import sys
sys.stdin = open("input.text","r")

n = int(input())
alphabet = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(n):
    now = list(input())
    now.reverse()
    length = 1
    for u in now:
        alphabet[ord(u)-65]+=length
        length *= 10

count = 0
for i in range(10):
    count += max(alphabet)*(9-i)
    alphabet.remove(max(alphabet))
print(count)