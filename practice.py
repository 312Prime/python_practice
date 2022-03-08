n,m = map(int,input().split())
cnt = 0
now = ''
check = ''
for i in range(n):
    list = input()
    if list[0] != check:
        check = list[0]
    else:
        cnt += 1
    for x in list:
        if now == x:
            cnt +=1
        else:
            now = x
    now = ''
print(cnt)   