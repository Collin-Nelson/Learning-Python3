'''
Created on May 6, 2019

@author: Collin Nelson
'''

Aseq = 'ABCABCABCABC'
Bseq = 'BABCBABCBABC'
Gseq = 'CCAABBCCAABB'

Acount = 0
Bcount = 0
Gcount = 0

N = int(input())
ans = input()

while N > len(Aseq):
    Aseq = Aseq + Aseq
    Bseq = Bseq + Bseq
    Gseq = Gseq + Gseq

for i in range(0, N):
    if Aseq[i] == ans[i]:
        Acount += 1
    if Bseq[i] == ans[i]:
        Bcount += 1
    if Gseq[i] == ans[i]:
        Gcount += 1


maxCount = max(Acount, Bcount, Gcount)
print(maxCount)

if maxCount == Acount:
    print("Adrian")
if maxCount == Bcount:
    print("Bruno")
if maxCount == Gcount:
    print("Goran")


