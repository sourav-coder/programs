# # # cook your dish here

# coded by ss


a,b,c=map(int,input().split())
taken=set()
final=set()
for _ in range(a):
        n=int(input())
        taken.add(n)
        
taken2=set()
for _ in range(b):
        n=int(input())
        if n in taken:final.add(n)
        else:taken2.add(n)
        
for _ in range(c):
        n=int(input())
        if n in taken or n in taken2:final.add(n)
    # print(check)
print(len(final))
    # print(taken)
check = sorted(final)
    # print(check)
for i in check:print(i)






