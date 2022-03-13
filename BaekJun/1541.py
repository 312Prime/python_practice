from dataclasses import replace
import sys
sys.stdin = open("input.text","r")

a=input()
b=[]
count=0

if a.find("-")== -1:
    a=a.replace("+", " ")
    a=map(int,a.split())
    count=sum(a)
else: 
    b=a[a.index("-")+1:]
    a=a[:a.index("-")]
    a=a.replace("+"," ")
    b=b.replace("-"," ")
    b=b.replace("+"," ")
    b=map(int,b.split())
    a=map(int,a.split())
    count=sum(a)-sum(b)
print(count)