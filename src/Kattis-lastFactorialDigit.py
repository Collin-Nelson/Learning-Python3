'''
Created on Apr 26, 2019

@author: Collin Nelson
'''

import time

time.sleep(2)

T = int(input())
N = []
ans = []

for i in range(0, T-1):
    N.append(int(input()))


for j in range(1, len(N)):
    a = 1
    for k in range(1, N[j]):
        a = a * k
    
    ans.append(a)

print(*ans)