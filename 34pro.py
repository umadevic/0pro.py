#a
uma,san=map(int,input().split())
psn=0
Lii=[]
for i in range(uma):
      Lii.append(input())
for i in range(uma):
      for j in range(san-1):
            if(Lii[i][j]!='R' and Lii[i][j+1]!='R'):
                  psn+=3
            elif(Lii[i][j]!='G' and Lii[i][j+1]!='G'):
                  psn+=5
print(psn)
