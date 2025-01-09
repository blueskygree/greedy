import sys
input=sys.stdin.readline

i=0

while True:
    l,p,v=map(int,input().split())

    if l==0 and p==0 and v==0:
        break
    
    i+=1

    count=(v//p)*l + min((v%p),l)

    print("Case %d: %d"%(i,count))