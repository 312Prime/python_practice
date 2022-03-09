n=int(input())
count=0

def calMoney(a,b):
    c=a%b
    return c

while True:
    if n==0:
        break
    if n>=50000:
        count += n//50000
        n = calMoney(n,50000)
        continue
    if n>=10000:
        count += n//10000
        n = calMoney(n,10000)
        continue
    if n>=5000:
        count += n//5000
        n = calMoney(n,5000)
        continue
    if n>=1000:
        count += n//1000
        n = calMoney(n,1000)
        continue
    if n>=500:
        count += n//500
        n = calMoney(n,500)
        continue
    if n>=100:
        count += n//100
        n = calMoney(n,100)
        continue
    if n>=50:
        count += n//50
        n = calMoney(n,50)
        continue
    if n>=10:
        count += n//10
        n = calMoney(n,10)
        continue
print(count)