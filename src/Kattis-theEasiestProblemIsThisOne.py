'''
Created on May 5, 2019

@author: Collin Nelson
'''

N = int(input())

while N != 0:   # loop through each line of input (N values)
    
    a = str(N)
    sumN = 0
    for i in range(0, len(a)):  #sum digits of N
        sumN = sumN + int(a[i:i+1])

    sumMN = 0
    M = 11
    while sumMN != sumN or sumMN == 0: #loop through each potential p to find m
        
        sumMN = 0
        b = str(M*N)
        for i in range(0, len(b)):  #sum digits of M*N
            sumMN = sumMN + int(b[i:i+1])
        
        M = M + 1
    
    print(M-1)
    N = int(input())