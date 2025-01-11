import sys
input=sys.stdin.readline

n=int(input())
link=list(map(int,input().split()))
cost=list(map(int,input().split()))

start=cost[0]
total=(start*link[0])
for i in range(1,len(link)):
    if start>=cost[i]:
        start=cost[i]
        total+=(cost[i]*link[i])
    elif start<cost[i]:
        total+=(start*link[i])

print(total)