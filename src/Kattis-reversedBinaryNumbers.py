'''
Created on May 5, 2019

@author: Collin Nelson
'''

inpt = str(bin(int(input())))
inpt = inpt[::-1]
print(int(inpt[0:len(inpt)-2], 2))