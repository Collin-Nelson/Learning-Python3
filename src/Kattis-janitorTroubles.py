'''
Created on Jul 21, 2019

@author: Collin Nelson
'''

inpts = input().split()

a = int(inpts[0])
b = int(inpts[1])
c = int(inpts[2])
d = int(inpts[3])

s = (a + b + c + d) / 2

area = ((s - a) * (s - b) * (s - c) * (s - d))**(1/2)
print(area)