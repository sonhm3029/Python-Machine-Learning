import numpy as np

A = np.array([[1, 5], [2, 3]])
B = np.array([[5, 8], [7, 3]])

def myFunc(A):
    return np.sum(np.max(A, axis=1)- np.min(A,axis=1));


def norm_fro(A):
    return np.sqrt(np.sum(A**2));
def dist_fro(A,B):
    return np.sum((A-B)**2)

