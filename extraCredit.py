# pete alonzi (datascientist@virginia.edu)
# a program to answer the fivethrityeight riddle
# 2020-05-17
# jed told me to

# vscode environment setup: https://code.visualstudio.com/docs/python/python-tutorial

#//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

import numpy as np
import matplotlib.pyplot as plt

# Set random seed if you want to reproduce
# np.random.seed(19680801)

N = 1000000 # number of die rolls (aka precision and runtime)
d = 20 # number of sides on the die

rollsREG = [] # list to contain the results of the rolls
rollsAOD = [] # list ot contain the results of AOD
rollsDOA = [] # list ot contain the results of DOA

#  Help: these helper functions are quick and lazy. please PR suggestions
def adv(x,y):
    ''' helper function to return advantage of two rolls '''
    advantage = x
    if y>x: advantage = y
    return advantage

def dis(x,y):
    ''' helper function to return disadvantage of two rolls '''
    disadvantage = x
    if y<x: disadvantage = y
    return disadvantage


for i in range(N):
    
    # Help: please pr a oneliner for this thatputs it into an interable
    # no list comprehension allowed, that stuff is lame
    r = np.random.randint(1,d+1,size=4)
    
    # record regular rolls
    rollsREG.extend(r)
    
    # record advantage of disadvantage
    rollsAOD.append(adv(dis(r[0],r[1]),dis(r[2],r[3])))

    # record disadvantage of advantage
    rollsDOA.append(dis(adv(r[0],r[1]),adv(r[2],r[3])))


# Help: I would love for someone to do the math and tell me where I should round off and/or what size error bars I should use on these numbers, I am too lazy to do the work
# Show the results
print()
print('last rolls',r)
print('regular expected roll                  ',np.mean(rollsREG))
print('advantage of disadvantage expected roll',np.mean(rollsAOD))
print('disadvantage of advantage expected roll',np.mean(rollsDOA))
print()


# Extra Credit, just make a histogram for each and pick the most probable
#plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()

# the histogram of the data
num_bins = 20
n, bins, patches = plt.hist(rollsREG, num_bins, density=1, facecolor='red', alpha=1, histtype='step', linewidth=4,label="d20")
n, bins, patches = plt.hist(rollsAOD, num_bins, density=1, facecolor='green', alpha=1, histtype='step',linewidth=4,label="Advantage of Disadvantage")
n, bins, patches = plt.hist(rollsDOA, num_bins, density=1, facecolor='blue', alpha=1, histtype='step',linewidth=4, label="Disadvantage of Advantage")

# make it understandable
plt.legend(loc=8)
ax.set_title("Extra Credit")
plt.xlabel('result of roll')
plt.ylabel('probability of result')



plt.show()

