from matplotlib import pyplot as plt
import random
population_ages=[]
for i in range(0,20,1):
    population_ages.append(random.randint(1,45))
print(population_ages)
bins=[]
for i in range(0,140,10):
    bins.append(i)
print(bins)
plt.hist(population_ages,bins,histtype='bar',rwidth=0.3)
plt.title('histogram')
plt.xlabel("X axis")
plt.ylabel('Y axis')
plt.legend()
plt.show()