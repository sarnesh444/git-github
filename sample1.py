from matplotlib import pyplot as plt
def pl():
    x=[1, 2, 3]
    y= [4, 5, 1]
    plt.title("sample")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.plot(x, y)
    plt.show() #to show
pl()