def cal10(i,l):
    if i<=l:
        return i+10
    else:
        return i-10

def cal5(i,l):
    if i<=l:
        return i+5
    else:
        return i-5

def cal1(i,l):
    if i<=l:
        return i+1
    else:
        return i-1

a,b=map(int,input().split())
count = 0
while True:
    if a==b:
        break
    if abs(a-b)>=10:
        count +=1
        a=cal10(a,b)
        continue
    if abs(a-b)>=5:
        sol1=cal10(a,b)
        sol2=cal5(a,b)
        if abs(b-sol1)<abs(b-sol2):
            a=sol1
        else:
            a=sol2
        count += 1
        continue
    else:
        sol1=cal5(a,b)
        sol2=cal1(a,b)
        if abs(b-sol1)<abs(b-sol2):
            count+=abs(b-sol1)+1
        else:
            count+=abs(b-sol2)+1
        break
print(count)