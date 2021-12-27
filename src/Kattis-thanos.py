'''
Created on May 7, 2019

@author: Collin Nelson
'''

import math

T = int(input())

for i in range(0, T):
    inpts = input().split()
    
    P = int(inpts[0])
    R = int(inpts[1])
    F = int(inpts[2])
    
    time = 0
    while P <= F:
        P = math.floor(P*R)
        time += 1
    
    print(time)