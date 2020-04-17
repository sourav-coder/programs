# cook your dish here
for _ in range(int(input())):

    for _ in range(int(input())):
        l,n,q=map(int,input().split())
        odd=0
        if n&1==1:odd=n//2+1
        else:odd=n//2
    
    
        even=n-odd
        if l==1:
            if q==1:print(even)
            else:print(odd)
        else:
            if q==1:print(odd)
            else:print(even)




            
