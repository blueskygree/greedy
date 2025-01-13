import sys
input=sys.stdin.readline

n=int(input())
data=list(map(int,input().split()))

data.sort(reverse=True)
start=data[0]
result=0

for i in range(1,len(data)):
    result+=(start+data[i])

print(result)