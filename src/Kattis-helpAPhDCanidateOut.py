'''
Created on May 7, 2019

@author: Collin Nelson
'''

N = int(input())

for i in range(0, N):
    inpt = input()
    
    if inpt[0:1] != "P":
        inpts = inpt.split('+')
        print(int(inpts[0])+int(inpts[1]))
    else:
        print('skipped')