import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    rank=[list(map(int,input().split())) for _ in range(n)]
    asc_rank=sorted(rank)
    top=0
    result=1

    for i in range(1,len(asc_rank)):
        if asc_rank[i][1]<asc_rank[top][1]:
            top=i
            result+=1
    print(result)