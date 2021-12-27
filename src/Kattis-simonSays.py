'''
Created on May 5, 2019

@author: Collin Nelson
'''

N = int(input())

for i in range(0, N):
    str = input()
    if str[0:10] == 'Simon says':
        print(str[11:len(str)])