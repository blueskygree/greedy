import sys
input=sys.stdin.readline

n,l=map(int,input().split())
li=list(map(int,input().split()))

li.sort()
start=li[0]
count=1

for i in li[1:]:
    if i in range(start,start+l):
        continue
    else:
        start=i
        count+=1

print(count)