'''
Created on May 4, 2019

@author: Collin Nelson
'''

n = int(input())
inpts = input().split()
count = 0

for i in range(0, n):
    t = int(inpts[i])
    if t < 0:
        count+=1

print(count)