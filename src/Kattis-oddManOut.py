'''
Created on May 6, 2019

@author: Collin Nelson
'''

N = int(input())

for i in range(0, N):
    G = int(input())
    inpts = input().split()
    
    list = []
    for j in range(0, len(inpts)):
        
        if (len(list) == 0 or inpts[j] 
            not in list):
            list.append(inpts[j])
            # inpts.remove(inpts[j])
        else:
            list.remove(inpts[j])
            #inpts.remove(inpts[j])
    
    print("Case #%d: %d" % (i+1, int(*list)))