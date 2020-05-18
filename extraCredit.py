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

def adv(r1,r2):
    ''' helper function to return advantage of two rolls '''
    return np.maximum(r1,r2)

def dis(r1,r2):
    ''' helper function to return disadvantage of two rolls '''
    return np.minimum(r1,r2)

rollsREG = np.random.randint(1, d+1, (N, 4))
rollsAOD = adv(dis(rollsREG[:,0], rollsREG[:,1]), dis(rollsREG[:,2], rollsREG[:,3]))
rollsDOA = dis(adv(rollsREG[:,0], rollsREG[:,1]), adv(rollsREG[:,2], rollsREG[:,3]))

# Help: I would love for someone to do the math and tell me where I should round off and/or what size error bars I should use on these numbers, I am too lazy to do the work
# Show the results
print()
print('last rolls',rollsREG[-1,:])
print('regular expected roll                  ',np.mean(rollsREG))
print('advantage of disadvantage expected roll',np.mean(rollsAOD))
print('disadvantage of advantage expected roll',np.mean(rollsDOA))
print()


# Extra Credit, just make a histogram for each and pick the most probable
#plt.style.use('fivethirtyeight')
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Extra Credit Plots')

binning = [ i+0.5 for i in range(21)]
xticks = range(0,21)
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
ax1.set_xticks(xticks, xlabels)

# generate the reverse CDF 
n, bins, patches = ax2.hist(rollsREG, binning, density=1, facecolor='red', alpha=1, histtype='step', linewidth=2,label="d20", cumulative=-1)
n, bins, patches = ax2.hist(rollsAOD, binning, density=1, facecolor='green', alpha=1, histtype='step',linewidth=2,label="Advantage of Disadvantage", cumulative=-1)
n, bins, patches = ax2.hist(rollsDOA, binning, density=1, facecolor='blue', alpha=1, histtype='step',linewidth=2, label="Disadvantage of Advantage", cumulative=-1)

# make it understandable
ax2.legend(loc='upper right')
ax2.set_title("Reverse CDF (aka probability to roll N or better)")
ax2.set_xlabel('result of roll')
ax2.set_ylabel('reverse cumulative probability')
ax2.set_xticks(xticks, xlabels)

plt.show()

