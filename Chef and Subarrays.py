
'''Chef likes problems involving arrays. Unfortunately, the last one he tried to solve didn't quite get solved.

Chef has an array A of N positive numbers. He wants to find the number of subarrays for which the sum and product of elements are equal.

Please help Chef find this number'''



# brute force solution
#coded by ss


for _ in range(int(input())):
  n=int(input())
  a=list(map(int,input().split()))
  c=0
  for i in range(len(a)):
    s=0
    p=1
    for j in range(i,-1,-1):
      s+=a[j]
      p*=a[j]
      if s==p:c+=1

  print(c)
