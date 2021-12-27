'''
Created on May 5, 2019

@author: Collin Nelson
'''

inpts = input().split()

a = inpts[0]
b = inpts[1]
c = inpts[2]

A = int(a)
B = int(b)
C = int(c)

if A+B == C:
    print(a + '+' + b + '=' + c)
elif B+C == A:
    print(a + '=' + b + '+' + c)
elif A+C == B:
    print(a + '=' + b + '-' + c)
elif A*B == C:
    print(a + '*' + b + '=' + c)
elif A == B*C:
    print(a + '=' + b + '*' + c)
elif A*C == B:
    print(a + '=' + b + '/' + c)