import numpy as np
from matplotlib.patches import Rectangle

def plot_samples(ax, xs, ys, title, legend=False):
    """ plot the datapoints 
    @params:
    ========
        ax: the plt axis
        xs: the input
        ys: the labels
        title: plot title
    """
    ax.set_title(title)
    x_offset = np.mean(xs[:, 0])
    y_offset = np.mean(xs[:, 1])
    ax.set_xlim(-1.0+x_offset, 1.0+x_offset)
    ax.set_ylim(-1.0+y_offset, 1.0+y_offset)
    pos_idxs = np.where(ys > 0)[0]
    neg_idxs = np.where(ys < 0)[0]
    if legend:
        ax.scatter(
            x=xs[pos_idxs][:, 0], 
            y=xs[pos_idxs][:, 1], 
            c='red', label='positive')
        ax.scatter(
            x=xs[neg_idxs][:, 0], 
            y=xs[neg_idxs][:, 1], 
            c='blue', label='negative')
        ax.legend()
    else:
        ax.scatter(
            x=xs[pos_idxs][:, 0], 
            y=xs[pos_idxs][:, 1], 
            c='red')
        ax.scatter(
            x=xs[neg_idxs][:, 0], 
            y=xs[neg_idxs][:, 1], 
            c='blue')

def plot_line(ax, color, weights, bias=0.0, label=None):
    """
    @params:
    ========
        ax: the plt axis
        color: line color
        weights, bias: y = w * x + b
        label: line label (optional)
    """
    x = np.linspace(-1,1,100)
    y = ( - bias - weights[0] * x) / weights[1]
    ax.plot(x, y, c=color, label=label)

def plot_affinities(ax, M, labels, title=None):
    # rearrange the data
    sorted_idxs = np.argsort(labels)
    M = M[sorted_idxs]
    labels = labels[sorted_idxs]
    # display the similarities
    ax.matshow(M)
    # draw the square to display groundtruth clusters
    rect_start = 0
    count = 0
    current_label = labels[0]
    for label in labels:
        if label != current_label:
            rect = Rectangle(
                (rect_start-0.5, rect_start-0.5), count, count,
                linewidth=2, edgecolor='r', facecolor='none')
            ax.add_patch(rect)
            current_label = label
            rect_start += count
            count = 0
        count += 1
    if count > 0:
        rect = Rectangle(
            (rect_start, rect_start), count, count,
            linewidth=2, edgecolor='r', facecolor='none')
        ax.add_patch(rect)
    
    # add title and fix axis
    if title is not None:
        ax.set_title(title)
    ax.axis('off')
