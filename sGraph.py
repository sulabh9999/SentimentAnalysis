import numpy as np
import matplotlib.pyplot as plt

def makeHistogram():
    n = 12
    X = np.arange(n)
    Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
    Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

    plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
    plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
    fig = plt.figure(figsize=(100,100))
    for x,y in zip(X,Y1):
        plt.text(x+0.4, y+0.05, '%.2f' % y, ha='center', va= 'bottom')

    plt.ylim(-1.25, +1.25)
    plt.show()


def makeGraph():
    people = ('A','B','C','D','E','F','G','H')
    segments = 4

    # generate some multi-dimensional data & arbitrary labels
    data = 3 + 10* np.random.rand(segments, len(people))
    percentages = (np.random.randint(5,20, (len(people), segments)))
    y_pos = np.arange(len(people))

    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)

    colors ='rgbwm'
    patch_handles = []
    left = np.zeros(len(people)) # left alignment of data starts at zero
    for i, d in enumerate(data):
        bar = ax.barh(y_pos, d, color=colors[i%len(colors)], align='center', left=left)
        patch_handles.append(bar)
        # accumulate the left-hand offsets
        left += d

    # go through all of the bar segments and annotate
    for j in range(len(patch_handles)):
        for i, patch in enumerate(patch_handles[j].get_children()):
            bl = patch.get_xy()
            x = 0.5*patch.get_width() + bl[0]
            y = 0.5*patch.get_height() + bl[1]
            ax.text(x,y, "%d%%" % (percentages[i,j]), ha='center')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(people)
    ax.set_xlabel('Distance')
    plt.show()