'''
Created on Nov 15, 2019

@author: Collin Nelson
'''

num = int(input())
j = 0
list = []

while(num != 0):
    
    lista = []
    listb = []
    front = True
    
    for i in range(0, num):
        if front == True:
            lista.append(input())
        else:
            listb.insert(0, input())
        front = not front
    
    j+=1
    num = int(input())
    
    
    list.append("SET " + str(j))
    for x in lista:
        list.append(x)
    for x in listb:
        list.append(x)
    
for x in list:
    print(x)