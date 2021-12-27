'''
Created on May 4, 2019

@author: Collin Nelson
'''

inpts = input().split()

N = int(inpts[0])
M = int(inpts[1])
list = [0] * (M+N+1)

for i in range(1, N):
    for j in range(1, M):
        list[i+j] = list[i+j] + 1

max = max(list)

for a in range(1, len(list)):
    if list[a] == max:
        print(a+1)