

# cook your dish here
#--coded by sourav sarkar--#

for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(str,input().split()))
    b=[]
    while(k>0):
        b.append(input())
        k-=1
    #print(b)

    for i in b:
        c=i.split(' ')
        #print(c)
        for i in range(len(a)):
            try:
                if a[i] in c:
                    #a.remove(a[i])
                    a[i]='YES'
            except:IndexError
    for i in a:
        if i=='YES':
            print(i,end=' ')
        else:print('NO',end=' ')
    print(' ')


