'''
Created on May 5, 2019

@author: Collin Nelson
'''

inpts = input().split()
A = int(inpts[0])
B = int(inpts[1])
C = int(inpts[2])

list = [abs(A-B), abs(B-C), abs(A-C)]
list.remove(max(list))
print(max(list)-1)