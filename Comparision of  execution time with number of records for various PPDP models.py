import matplotlib.pyplot as plt
from pylab import *
rc('axes', linewidth=2)
number_of_records=[1000,5000,10000,30000,50000]
kc_slice=[13,20,32,60,100]
kci_slice=[9,18,25,50,95]
novel_kci_slice=[9,19,25,48,90]
optimal_kci_slice=[3,5,7,20,35]
slamsa=[14,21,36,65,120]
PK_angelization=[10,14,22,55,107]
onem_generalization=[4,6,8,22,40]
labels=['KC-slice','KCi - slice','Novel KCi - slice','Optimal KCi - slice','SLAMSA','(P,K)-Angelization','1: M Generalization']
plt.plot(number_of_records,kc_slice)
plt.plot(number_of_records,kci_slice)
plt.plot(number_of_records,novel_kci_slice)
plt.plot(number_of_records,optimal_kci_slice)
plt.plot(number_of_records,slamsa)
plt.plot(number_of_records,PK_angelization)
plt.plot(number_of_records,onem_generalization)
plt.title("Comparision of  execution time with number of records for various PPDP models",weight='bold')
fontsize = 14
ax = gca()
for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontsize(fontsize)
    tick.label1.set_fontweight('bold')
for tick in ax.yaxis.get_major_ticks():
    tick.label1.set_fontsize(fontsize)
    tick.label1.set_fontweight('bold')

plt.xlabel('Number of records',weight='bold')
plt.ylabel('Time in sec',weight='bold')
leg=plt.legend(labels)
leg_lines=leg.get_lines()
leg_texts=leg.get_texts()
plt.setp(leg_lines, linewidth=12)
plt.setp(leg_texts, fontsize='x-large')
plt.show()







