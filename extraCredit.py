# pete alonzi (datascientist@virginia.edu) (alonzi on github)
# contributors: [ wshanley, danielcmccarthy ]
# a program to answer the fivethrityeight riddle
# 2020-05-17
# patch 1: 2020-05-18
# jed told me to

# vscode environment setup: https://code.visualstudio.com/docs/python/python-tutorial

#//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

import numpy as np
import matplotlib.pyplot as plt

# Set random seed if you want to reproduce
# np.random.seed(19680801)

N = 1000000 # number of die rolls (aka precision and runtime)
d = 20 # number of sides on the die

def adv(r1,r2):
    ''' helper function to return advantage of two rolls (flavor rename)'''
    return np.maximum(r1,r2)

def dis(r1,r2):
    ''' helper function to return disadvantage of two rolls (flavor rename)'''
    return np.minimum(r1,r2)

roll4 = np.random.randint(1, d+1, (N, 4))
rollsREG = [ i for r in roll4 for i in r ] # unroll for plotting
rollsAOD = adv(dis(roll4[:,0], roll4[:,1]), dis(roll4[:,2], roll4[:,3]))
rollsDOA = dis(adv(roll4[:,0], roll4[:,1]), adv(roll4[:,2], roll4[:,3]))

# Help: I would love for someone to do the math and tell me where I should round off and/or what size error bars I should use on these numbers, I am too lazy to do the work
# Show the results
print()
print('last rolls',rollsREG[-4:])
print('regular expected roll                  ',np.mean(rollsREG))
print('advantage of disadvantage expected roll',np.mean(rollsAOD))
print('disadvantage of advantage expected roll',np.mean(rollsDOA))
print()


# Extra Credit, just make a histogram for each and pick the most probable
#plt.style.use('fivethirtyeight')
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Extra Credit Plots')

binning = [ i+0.5 for i in range(d+1)]

xticks = range(0,d+1)
xlabels = [i if i%5 == 0 else "" for i in xticks]

# generate PDF
n, bins, patches = ax1.hist(rollsREG, binning, density=1, facecolor='red', alpha=1, histtype='step', linewidth=2,label="d20")
n, bins, patches = ax1.hist(rollsAOD, binning, density=1, facecolor='green', alpha=1, histtype='step',linewidth=2,label="Advantage of Disadvantage")
n, bins, patches = ax1.hist(rollsDOA, binning, density=1, facecolor='blue', alpha=1, histtype='step',linewidth=2, label="Disadvantage of Advantage")

# make it understandable
ax1.legend(loc=8)
ax1.set_title("PDF")
ax1.set_xlabel('result of roll')
ax1.set_ylabel('probability of result')
#updated set_xticks statement to align ticks with integers set from xlabels
ax1.set_xticks(range(0, 25, 5))
#ax1.set_xticks(xticks, xlabels)

# generate the reverse CDF 
n, bins, patches = ax2.hist(rollsREG, binning, density=1, facecolor='red', alpha=1, histtype='step', linewidth=2,label="d20", cumulative=-1)
n, bins, patches = ax2.hist(rollsAOD, binning, density=1, facecolor='green', alpha=1, histtype='step',linewidth=2,label="Advantage of Disadvantage", cumulative=-1)
n, bins, patches = ax2.hist(rollsDOA, binning, density=1, facecolor='blue', alpha=1, histtype='step',linewidth=2, label="Disadvantage of Advantage", cumulative=-1)

# make it understandable
ax2.legend(loc='upper right')
ax2.set_title("Reverse CDF (aka probability to roll N or better)")
ax2.set_xlabel('result of roll')
ax2.set_ylabel('reverse cumulative probability')
#same update made for ax2 as for ax1 to align xticks to xlabels
ax2.set_xticks(range(0,25, 5))

plt.show()

