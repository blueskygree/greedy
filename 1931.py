import sys
input=sys.stdin.readline

n=int(input())
data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))

data.sort(key=lambda x : (x[1],x[0]))

end=0
cnt=0

for newstart,newend in data:
    if end>newstart:
        continue
    elif end<=newstart:
        end=newend
        cnt+=1

print(cnt)