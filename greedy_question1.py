import sys
input=sys.stdin.readline

N=int(input())
Data=list(map(int,input().split()))

Data.sort()
result=0
count=0

for i in Data:
    count+=1
    if count>=i:
        result+=1
        count=0
print(result)