'''
Created on Nov 24, 2019

@author: Collin Nelson
'''


nums = input().split()
print(len(nums))

counted = []
count = []

for i in range(0, len(nums)):
    if counted.count(float(nums[i])) == 0:
        counted.append(float(nums[i]))
        count.append(1)
        for j in range(i+1, len(nums)):
            if float(nums[i]) == float(nums[j]):
                count[counted.index(float(nums[i]))] = count[counted.index(float(nums[i]))]+1
                
    
    
    
    '''
    input full list
    loop through list and for each value in the list, loop through again
    count the number of times that values occurs, store value and number in a list
    then remove every occurence of the value
    '''
print(len(nums), nums)
print(len(counted), counted)
print(len(count), count)
