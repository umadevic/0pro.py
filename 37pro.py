#a
y2 = int(input())
p = [ int(x) for x in input().split()]
y2 = len(p)
if y2==1 :
    print(1)
   
cnt = 0
for i in range(1,y2-1) :
    if ((p[i] > p[i-1]) and (p[i] > p[i+1])) or ((p[i] < p[i-1]) and (p[i] < p[i+1])):
        cnt += 1
print(cnt)
