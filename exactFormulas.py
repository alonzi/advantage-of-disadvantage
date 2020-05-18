import numpy as np
import matplotlib.pyplot as plt

# Cute formulas for advantage and disadvantage pdfs. Not used, but I like them.
def adv_pdf(i, N):
    """ probability of rolling i as max of two N-dice """
    if i > N or i < 1:
        return 0
    else:
        return (2*i-1.)/(N**2)

def dis_pdf(i, N):
    """ probability of rolling i as min of two N-dice """
    return adv_pdf(N+1-i,N)

N = 20
dis_of_adv,adv_of_dis = np.zeros(N), np.zeros(N) 

for a in range(N):
    for b in range(N):
        adv1 = max(a,b)
        dis1 = min(a,b)
        for c in range(N):
            for d in range(N):
                adv2 = max(c,d)
                dis2 = min(c,d)
                dis_of_adv[min(adv1,adv2)] += 1.
                adv_of_dis[max(dis1,dis2)] += 1.

normal = np.array([1./N]*N) 
dis_of_adv = dis_of_adv / N**4
adv_of_dis = adv_of_dis / N**4

# print expected values
print("normal roll EV: {0}".format(sum(np.arange(1,N+1) * normal)))
print("dis_of_adv  EV: {0}".format(sum(np.arange(1,N+1) * dis_of_adv)))
print("adv_of_dis  EV: {0}".format(sum(np.arange(1,N+1) * adv_of_dis)))

fig, (ax1,ax2) = plt.subplots(1,2)

barWidth = 0.25
r1 = range(1,N+1)
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
xticks = range(0,N+1)
xlabels = [i if i%5 == 0 else "" for i in xticks]

ax1.bar(r1, dis_of_adv, color='blue', width=barWidth, edgecolor='white', label='dis_of_adv')
ax1.bar(r2, adv_of_dis, color='green', width=barWidth, edgecolor='white', label='adv_of_dis')
ax1.bar(r3, normal, color='red', width=barWidth, edgecolor='white', label='normal')

ax1.legend()
ax1.set_title("PDF")
ax1.set_xlabel("roll result")
ax1.set_ylabel("probability of result")
ax1.set_xticks(xticks, xlabels)

def rev_cdf(arr):
    return np.array([sum(arr[i:]) for i in range(len(arr))])

ax2.plot(r1, rev_cdf(dis_of_adv), color='blue', label='dis_of_adv')
ax2.plot(r1, rev_cdf(adv_of_dis), color='green', label='adv_of_dis')
ax2.plot(r1, rev_cdf(normal), color='red', label='normal')

ax2.legend()
ax2.set_title("Reverse CDF (probability to roll at least x)")
ax2.set_xlabel("roll result")
ax2.set_ylabel("reverse cumulative probability")
ax2.set_xticks(xticks, xlabels)

plt.show()
