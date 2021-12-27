'''
Created on Jul 21, 2019

@author: Collin Nelson
'''

inpts = input().split()
a1 = int(inpts[0])
b1 = int(inpts[1])
c1 = int(inpts[2])

inpts = input().split()
a2 = int(inpts[0])
b2 = int(inpts[1])
c2 = int(inpts[2])

inpts = input().split()
a3 = int(inpts[0])
b3 = int(inpts[1])
c3 = int(inpts[2])

grid = [[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]]

distance = 0

# findCoordinates() function using nested loops to get 
# a coordinate pair for each number 1 through 9
def findCoordinates(grid, num):
    
    coords = [0, 0]
    
    for i in range(1, 3):
        for j in range(1, 3):
            if grid[i][j] == num:
                coords = [i, j]
    
    return coords
# end findCordinates()

for i in range(1, 9):
    Acoords = findCoordinates(grid, i)
    Bcoords = findCoordinates(grid, i+1)
    distance = distance + ( (Bcoords[0] - Acoords[0])**2
                        + (Bcoords[1] - Acoords[1])**2)**(1/2)
    
print(distance)
# then calculate the distance between each coordinate pair using pythagorian theorum


    
    