#a
o = int(input())
r = [ int(x) for x in input().split()]
o = len(r)
u = 0
for i in range(0,o-2):
    for j in range(i+1, o-1):
        for k in range(j+1, o):
            if r[i] > r[j] > r[k] :
                u =u+ 1
print(u)
