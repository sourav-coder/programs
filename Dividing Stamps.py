# cook your dish here

n=int(input())
a=list(map(int,input().split()))
s=sum(a)
s1=(n*(n+1))//2

if s==s1:print('YES')
else:print('NO')
