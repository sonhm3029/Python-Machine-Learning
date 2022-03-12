import numpy as np

A = np.array([[1, 2, 3],
       [4, 5, 6]])
B = np.array([[5, 8], [7, 3]])

def myFunc(A):
    return np.sum(np.max(A, axis=1)- np.min(A,axis=1));


def norm_fro(A):
    return np.sqrt(np.sum(A**2));
def dist_fro(A,B):
    return np.sum((A-B)**2)

# print(A.reshape(3,-1,order='C'));

# print(np.reshape(A,(3,-1),order='F'));


# x = np.arange(1,13);
# C = (x.reshape(4,-1,order='F')).reshape(3,-1);

# print(C);


def zero_mean(A):
    v = A.shape[0];
    h = A.shape[1];
    return (
        A.T - (np.mean(A,axis=1))).T;

d = zero_mean(A);
print(np.random.seed(10))

help(np.random.permutation)
