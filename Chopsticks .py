# cook your dish here

# coded by ss
n,d=map(int,input().split())
a=[]
for _ in range(n):
    a.append(int(input()))

a.sort()

i=0
c=0
while i<n-1:
    if a[i+1]-d <=a[i]:
        c+=1
        i+=2
    else:i+=1

print(c)
