#a
import sys,string
def cfreq(m) :
    din = {}
    for c in m :
        din[c] = din.get(c,0) + 1
    return din
 
m = input()
n = len(m)
din = cfreq(m)
Lk = list(din.keys())
#print(din,Lk)
 
for j in range(n-2,-1,-1) :
    #print('len = ', j+1)
    for c in Lk :
        kin = 0
        for i in range(0,n-j) :
            li, ri = i,j+i
            s2 = m[li:ri + 1]
            #print(c,s2)
            if c in s2 :
                kin += 1
        if kin == n-j :
            #print('c,kin',c,kin)
            c2 = c
            kin2 = kin
            len2 = j+1
print(len2)
