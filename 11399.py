import sys
input=sys.stdin.readline

n=int(input())
data=list(map(int,input().split()))

data.sort()
mid=0
result=0

for i in range(len(data)):
    mid+=data[i]
    result+=mid
    
print(result)