import sys
input=sys.stdin.readline

n,k=map(int,input().split())
data=[int(input()) for _ in range(n)]
data.sort(reverse=True)

count=0

for i in data:
    if k>=i:
        count+=k//i
        k%=i

    if k<=0:
        break

print(count)