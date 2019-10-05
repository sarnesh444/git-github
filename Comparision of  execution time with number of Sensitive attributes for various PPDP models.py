import matplotlib.pyplot as plt
from pylab import *
rc('axes', linewidth=2)
number_of_sensitive_attributes=[2,3,4,5]
kc_slice=[9,14,19,20]
kci_slice=[6,8,10,11]
novel_kci_slice=[6,7,9,11]
optimal_kci_slice=[3,4,5,7]
slamsa=[7,15,20,25]
PK_angelization=[10,11,11,11]
onem_angelization=[4,7,9,9]
labels=['KC-slice','KCi - slice','Novel KCi - slice','Optimal KCi - slice','SLAMSA','(P,K)-Angelization','1: M Generalization']
plt.plot(number_of_sensitive_attributes,kc_slice)
plt.plot(number_of_sensitive_attributes,kci_slice)
plt.plot(number_of_sensitive_attributes,novel_kci_slice)
plt.plot(number_of_sensitive_attributes,optimal_kci_slice)
plt.plot(number_of_sensitive_attributes,slamsa)
plt.plot(number_of_sensitive_attributes,PK_angelization)
plt.plot(number_of_sensitive_attributes,onem_angelization)
plt.title("Comparision of  execution time with number of Sensitive attributes for various PPDP models",weight='bold')
fontsize = 14
ax = gca()
for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontsize(fontsize)
    tick.label1.set_fontweight('bold')
for tick in ax.yaxis.get_major_ticks():
    tick.label1.set_fontsize(fontsize)
    tick.label1.set_fontweight('bold')
leg=plt.legend(labels)
plt.xlabel("Number of records",weight='bold')
plt.ylabel("Time in sec",weight='bold')
leg_lines=leg.get_lines()
leg_texts=leg.get_texts()
plt.setp(leg_lines, linewidth=12)
plt.setp(leg_texts, fontsize='x-large')
plt.show()




