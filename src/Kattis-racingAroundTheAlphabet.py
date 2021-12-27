'''
Created on May 6, 2019

@author: Collin Nelson
'''

N = int(input())

LetTime = (60*3.14159265/28)/15
LetOrder = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '"

for i in range(0, N):
    
    str = input()
    time = len(str)     # account for each pickup
    
    for j in range(0, len(str)-1):
        pos1 = 0;
        pos2 = 0
        for m in range(0, 28):
            
            debA = str[j]
            debB = str[j+1]
            debC = LetOrder[m]
            
            if str[j] == LetOrder[m]:
                pos1 = m
            if str[j+1] == LetOrder[m]:
                pos2 = m
        
        distance = abs(pos2-pos1)
        if distance > 14:
            distance = 28 - distance
        
        time = time + distance*LetTime
    
    print(time)