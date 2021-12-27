'''
Created on May 5, 2019

@author: Collin Nelson
'''

key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
inpt = input().split()

while inpt[0] != '0':
    
    rot = int(inpt[0])
    str = inpt[1][::-1]    # reverses string
    newStr = ''
    
    for i in str:
        newStr = newStr + key[key.index(i)+rot]  #shift
    
    inpt = input().split()
    print(newStr)