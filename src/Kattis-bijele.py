'''
Created on Apr 26, 2019

@author: Collin Nelson
'''

pieces = input().split()

changes = []

changes.append(1 - int(pieces[0]))
changes.append(1 - int(pieces[1]))
changes.append(2 - int(pieces[2]))
changes.append(2 - int(pieces[3]))
changes.append(2 - int(pieces[4]))
changes.append(8 - int(pieces[5]))


print(*changes)