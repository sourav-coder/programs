# cook your dish here
# python programs by sourav


# code

t,st=map(str,input().split())
s=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

punc={'.',',','!','?',' '}

for _ in range(int(t)):
    p=input().replace('_',' ')

    new=''
    for i in p:
        if i.isupper():
            new+=st[s.index(i.lower())].upper()
        elif i in punc:
            new+=i
        else:
            new+=st[s.index(i)]
    print(new)


