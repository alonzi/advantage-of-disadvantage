# pete alonzi (datascientist@virginia.edu)
# a program to answer the fivethrityeightriddle
# 2020-05-17
# jed told me to

#//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

import random
import numpy as np

N = 10000000 # number of die rolls (aka precision and runtime)
d = 20 # number of sides on the die

rollsREG = [] # list to contain the results of the rolls
rollsAOD = [] # list ot contain the results of AOD
rollsDOA = [] # list ot contain the results of DOA

#  Help: these helper functions are quick and lazy. please PR suggestions
def adv(r1,r2):
    ''' helper function to return advantage of two rolls '''
    advantage = r1
    if r2>r1: advantage= r2
    return advantage

def dis(r1,r2):
    ''' helper function to return disadvantage of two rolls '''
    disadvantage = r1
    if r2<r1: disadvantage=r2
    return disadvantage


for i in range(N):
    
    # Help: please pr a oneliner for this thatputs it into an interable
    # no list comprehension allowed, that stuff is lame
    r1 = random.randint(1,d)
    r2 = random.randint(1,d)
    r3 = random.randint(1,d)
    r4 = random.randint(1,d)

    # record regular rolls
    rollsREG.extend([r1,r2,r3,r4])
    
    # record advantage of disadvantage
    rollsAOD.append(adv(dis(r1,r2),dis(r3,r4)))

    # record disadvantage of advantage
    rollsDOA.append(dis(adv(r1,r2),adv(r3,r4)))


# Help: I would love for someone to do the math and tell me where I should round off and/or what size error bars I should use on these numbers
# Show the results
print()
print('regular expected roll                  ',np.mean(rollsREG))
print('advantage of disadvantage expected roll',np.mean(rollsAOD))
print('disadvantage of advantage expected roll',np.mean(rollsDOA))
print()