'''
Created on May 5, 2019

@author: Collin Nelson
'''

inpts = input()
output = ''

for i in range(0, len(inpts)):
    char = ord(inpts[i: i+1])
    if char > 64 and char < 91:
        output = output + chr(char)

print(output)