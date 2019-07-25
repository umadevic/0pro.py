#a
y=input()
f=0
for x in range(0,len(y)-1):
  for j in range(x+1,len(y)):
    if y[x]<y[j]:
      f=1
      print(y[j:])
      break
  if f==1:
    break
  else:
      print(y)
