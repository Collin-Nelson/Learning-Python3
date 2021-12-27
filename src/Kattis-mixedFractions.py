'''
Created on May 6, 2019

@author: Collin Nelson
'''

inpts = input().split()

while inpts[0] != "0":
    
    num = int(inpts[0])
    den = int(inpts[1])
    
    whl = num // den
    num -= den*whl
    
    print("%d %d / %d" % (whl, num, den))
    
    inpts = input().split()