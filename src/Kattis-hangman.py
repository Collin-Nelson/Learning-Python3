'''
Created on May 17, 2019

@author: Collin Nelson
'''

word = input()
guesses = input()

wrong = 0

for i in range(0, len(guesses)-1):    # loop through guesses
    elem = guesses[i:i+1]
    
    length = len(word)
    for j in range(0, len(word)-1):
        if word[j] is elem:
            word = word[0:j] + word[j+1]
    if length is len(word):
        wrong += 1
    
    if wrong >= 10:         # lose if wrong 10 times
        print("LOSE")
    elif len(word) is 0:    # win if length of word is 0
        print("WIN")

print("end")