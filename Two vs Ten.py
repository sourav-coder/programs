

# --coded by sourav sarkar--

def fun(n,c):

    if n%10==0:return c
    elif c==20:return -1
    else:
        c+=1
        return fun(n*2,c)


for _ in range(int(input())):
    x=int(input())
    c=0
    print(fun(x,c))




