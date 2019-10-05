from matplotlib import pyplot as plt

def pie_plot():
    slices=[7,2,2,13]
    act=['sleeping','eating','working','playing']
    colors=['c','m','r','b']

    plt.pie(slices,labels=act,colors=colors,startangle=90,shadow=True,explode=(0,0,0,0.1),autopct='%1.1f%%')

    plt.title("Pie plot")
    plt.show()
pie_plot()