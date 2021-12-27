'''
Created on May 5, 2019

@author: Collin Nelson
'''

K = int(input())
Acount = 1
Bcount = 0

for i in range(0, K):
    newB = Acount + Bcount
    newA = Bcount
    
    Acount = newA
    Bcount = newB

print(str(Acount) +' '+ str(Bcount))