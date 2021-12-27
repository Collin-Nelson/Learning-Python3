'''
Created on Apr 26, 2019

@author: Collin Nelson
'''

nums = input().split()

A = int(nums[0][2: 3] + nums[0][1: 2] + nums[0][0: 1])
B = int(nums[1][2: 3] + nums[1][1: 2] + nums[1][0: 1])

if A > B:
    print(A)
else:
    print(B)