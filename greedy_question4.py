import sys
input=sys.stdin.readline

N=int(input())
Data=list(map(int,input().split()))
Data.sort()

target=1

for i in Data:
    if target < i:
        break
    target+=i

print(target)