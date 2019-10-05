from matplotlib import pyplot as plt
from matplotlib import  style

x=[12,5,8]
y=[3,7,9]

x1=[14,2,8]
y1=[9,5,3]

plt.bar(x,y,label="Bar graph")
plt.bar(x1,y1,label="bar graph green")

plt.legend()

plt.xlabel("number")
plt.ylabel("height")

plt.show()

#difference between bar plot and histogram ,histogram uses quantitative variables,bar plot uses categorial variables