import sys
input=sys.stdin.readline

n=int(input())
list_a=list(map(int,input().split()))
list_b=list(map(int,input().split()))
result=0 

for i in range(n):
    result+=min(list_a)*max(list_b)
    list_a.pop(list_a.index(min(list_a)))
    list_b.pop(list_b.index(max(list_b)))

print(result)