import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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


# import matplotlib.pyplot as plt
# import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.figure(200)

plt.plot([1,3,2,5,9])
# plt.show()

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.figure()
plt.plot(x, y)

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()

arr = [1,2,3,4];

ok = pd.Series(arr);

print(type(ok));

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar[0])