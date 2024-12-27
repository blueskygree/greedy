import sys
input=sys.stdin.readline

N,M=map(int,input().split())
Data=list(map(int,input().split()))


array=[0]*11

for x in Data:
    array[x]+=1

result=0

for i in range(1,M+1):
    N-=array[i]
    result+=array[i]*N

print(result)