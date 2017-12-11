#! /usr/bin/env python3

import pickle
import numpy as np
import matplotlib.pyplot as plt
import itertools


def plotMatrix(matrix, labels, title='Matrix', cmap=plt.cm.Blues, rotateX=90):
    threshold = matrix.max()/2
    plt.imshow(matrix, cmap)
    plt.title(title)
    plt.colorbar()
    plt.xticks(np.arange(len(labels)), labels, rotation=rotateX)
    plt.yticks(np.arange(len(labels)), labels)
    fmt = '.2f'
    for i, j in itertools.product(range(matrix.shape[0]), range(matrix.shape[1])):
        plt.text(j, i, format(matrix[i, j], fmt), horizontalalignment="center", color = "black" \
        if matrix[i,j] < threshold else "white")
    plt.show()


if __name__ == '__main__':

    LAMatrix = pickle.load(open('Matrix.pkl', 'rb'))
    labels = pickle.load(open('labels.pkl', 'rb'))

    plotMatrix(LAMatrix, labels, title="Keyword Similarity Matrix", rotateX=90)
