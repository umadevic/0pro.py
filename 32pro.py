#a
um,sa=map(int,input().split())
yu=[]
for i in range(0,um):
    mn=[int(sv) for sv in input().split()]
    yu.append(sorted(mn))
for i in range(0,len(yu[0])):
  #print(yu[i])
  for j in range(0,len(yu)-1):
    if yu[j][i]>yu[j+1][i]:
      yu[j][i],yu[j+1][i]=yu[j+1][i],yu[j][i]
for i in yu:
  print(*i)
