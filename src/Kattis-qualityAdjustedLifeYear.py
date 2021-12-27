'''
Created on May 4, 2019

@author: Collin Nelson
'''

N = int(input())

QALY = 0

for i in range(0, N):
    inputs = input().split()
    q = float(inputs[0])
    y = float(inputs[1])
    QALY += q*y

print(QALY)