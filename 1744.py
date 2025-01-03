import sys
input=sys.stdin.readline

plus=[]
minus=[]
result=0

n=int(input())
for i in range(n):
    data=int(input())
    
    if data>1:
        plus.append(data)
    elif data<=0:
        minus.append(data)
    else:
        result+=data

plus.sort(reverse=True)
minus.sort()

for i in range(0,len(plus),2):
    if i+1>=len(plus):
        result+=plus[i]
    else:
        result+=(plus[i]*plus[i+1])

for i in range(0,len(minus),2):
    if i+1>=len(minus):
        result+=minus[i]
    else:
        result+=(minus[i]*minus[i+1])

print(result)