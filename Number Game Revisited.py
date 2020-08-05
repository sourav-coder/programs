# cook your dish here

for _ in range(int(input())):
    m=int(input())
    n=(m-1)/4+1
    # print(n)
    if str(n)[-1] == '0' and str(n)[-2]=='.':print('ALICE')
    else:print('BOB')




