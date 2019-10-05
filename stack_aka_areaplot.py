from matplotlib import  pyplot as plt
def stackarea():
    days=[1,2,3,4,5]

    eating=[2,3,4,3,2]
    sleeping=[7,8,6,11,7]
    playing=[8,5,7,8,13]
    working=[7,8,7,2,2]


    plt.plot([],[], color='m', label='sleeping', linewidth=5)
    plt.plot([],[],color='c', label='eating', linewidth=5)
    plt.plot([],[], color='r', label='working', linewidth=5)
    plt.plot([],[], color='k', label='playing', linewidth=5)

    #all the above four lines are used for generating a skeleton for the legend since no parameters have been passed it does not generate any lines
    plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','k'])

    plt.title("Stack area")
    plt.legend()
    plt.show()
stackarea()