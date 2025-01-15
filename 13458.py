import sys
input=sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))
B,C=map(int,input().split())

count=n

for i in range(len(A)):
    A[i]-=B
    if A[i]>0:
        count+=(A[i]//C)
        if A[i]%C != 0:
            count+=1

print(count)