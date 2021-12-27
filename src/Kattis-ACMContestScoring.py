'''
Created on Jul 21, 2019

@author: Collin Nelson
'''

correct = 0
time = 0
wrongs = ['']

inpts = input().split()

while inpts[0] != "-1":

    if inpts[2] == "right":
        correct = correct + 1
        time = time + int(inpts[0])
        while inpts[1] in wrongs:      # check list of wrong solutions
            time = time + 20        # add 20 to time for each wrong answer
            wrongs.remove(inpts[1]) # then remove that answer
    else:
        wrongs.append(inpts[1])
    
    inpts = input().split()
    
print(correct, time)
print(wrongs)

# every time there's a wrong answer, add that letter to a list.
# if there's a right answer for that letter, check the list for the wrong answer
# add 20 to time, remove the wrong answer from the list, and check again
# until there are no more instances of that wrong answer