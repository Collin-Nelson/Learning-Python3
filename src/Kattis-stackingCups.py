'''
Created on May 5, 2019

@author: Collin Nelson
'''

N = int(input())
Rlist = []
Clist = []

for i in range(0, N):
    inpts = input().split()
    f = inpts[0]
    s = inpts[1]
    
    if ord(f[0:1]) > 96:
        C = f
        R = int(s)
    else:
        C = s
        R = int(f)/2
    
    Rlist.append(R)
    Clist.append(C)

while len(Rlist) > 0:
    indx = Rlist.index(min(Rlist))
    print(Clist.pop(indx))
    Rlist.pop(indx)
