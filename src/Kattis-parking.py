'''
Created on May 6, 2019

@author: Collin Nelson
'''

t = int(input())


for i in range(0, t):
    
    n = int(input())
    inpts = input().split()
    
    stores = [None] * n
    for j in range(0, n):
        stores[j] = int(inpts[j])
    
    ma = max(stores)
    mi = min(stores)
    
    distance = 2*(ma-mi)
    print(distance)