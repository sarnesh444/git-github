from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x=[5,8,10]
y=[3,4,5]

x1=[3,6,9]
y1=[2,4,6]

plt.plot(x1,y1,'g',label="line one",linewidth=4)  #here g specifies color #plt.plot() plots a linear graph aka line graph cannot draw other type of graphs
plt.plot(x,y,'c',label="line two",linewidth=4)    #same

plt.title("sample2")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.grid(True,color='k')

plt.legend()  #gives a desciption of lines plotted

plt.show()