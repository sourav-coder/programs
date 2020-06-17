

# codechef --- easy 

for _ in range(int(input())):
    n,k=map(int,input().split())

    a=sorted(list(map(int,input().split())))

    p,q=abs(sum(a[:k])-sum(a[k:])),abs(sum(a[:len(a)-k])-sum(a[len(a)-k:]))

    print(max(p,q))




