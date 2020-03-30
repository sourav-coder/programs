
# cook your dish here
''
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=[]
    for i in range(1,n+1):
        if a.count(i)==0:
            b.append(i)
    c=[]
    d=[]
    for i in range(len(b)):
        if i&1==0:c.append(b[i])
        else:d.append(b[i])
    if c!=[]:
        for i in c:print(i,end=' ')
        print()
    else:print('\n')
    if d!=[]:
        for i in d:print(i,end=' ')
        print()
    else:print('\n')



