from matplotlib import  pyplot as plt
def scat():
    x=[1,2,3,4,5,6,7,8]
    y=[5,3,2,4,1,2,5,7]

    plt.scatter(x,y,label="scatter plot",color='k')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("scatter plot")
    plt.legend()
    plt.show()
scat()