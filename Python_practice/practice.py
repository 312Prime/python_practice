import sys
sys.stdin = open("/Users/sangillee/Python_practice/Python_practice/input.txt", "r")

line = list(map(int, sys.stdin.readline().split()))

print(line)