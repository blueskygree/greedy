import sys
input=sys.stdin.readline

n=int(input())
data=[]
for _ in range(n):
    data.append(int(input()))

data.sort()
li=[]

for i in data:
    li.append(i*n)
    n-=1

print(max(li))