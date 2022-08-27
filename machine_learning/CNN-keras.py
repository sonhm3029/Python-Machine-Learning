from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import np_utils
import numpy as np
import matplotlib.pyplot as plt

""" Lib -description
    Dense (num_nodes, activation=activate_func): fully connected layer 
    Flatten: Flatten images matrix

    Layer:
        Conv2D: Convolution layer
        MaxPooling2D: Max pooling kernel layer


This is a dataset of 50,000 32x32 color training images and 10,000 test images, labeled over 10 categories. See more info at the

Label	Description
0	airplane
1	automobile
2	bird
3	cat
4	deer
5	dog
6	frog
7	horse
8	ship
9	truck

x_train: uint8 NumPy array of grayscale image data with shapes (50000, 32, 32, 3),
containing the training data. Pixel values range from 0 to 255.

y_train: uint8 NumPy array of labels (integers in range 0-9) with shape (50000, 1) for the training data.

x_test: uint8 NumPy array of grayscale image data with shapes (10000, 32, 32, 3),
containing the test data. Pixel values range from 0 to 255.

y_test: uint8 NumPy array of labels (integers in range 0-9) with shape (10000, 1) for the test data.

"""

# loading data
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

print(f"X_train size {X_train.shape}")
print(f"y_train size")

# Validation set
(X_val, y_val) = X_train[40000:,:], y_train[40000:]
# Training set
(X_train, y_train) = X_train[:40000,:], y_train[:40000,:]

# reshape data
X_train = X_train.reshape(X_train.shape[0], 32, 32, 3)
X_val = X_val.reshape(X_val.shape[0], 32, 32, 3)
X_test = X_test.reshape(X_test.shape[0], 32, 32, 3)

# One-hot coding
Y_train = np_utils.to_categorical(y_train,10)
Y_test = np_utils.to_categorical(y_test, 10)
Y_val = np_utils.to_categorical(y_val, 10)

print(f"Y_train for 10: {Y_train[:10]}")
# define model
model = Sequential()

# Add convolution layer and pooling layer
model.add(Conv2D(32, (5, 5), activation='relu', input_shape=(32,32,3)))
model.add(Conv2D(32, (5,5), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
# model.add(Conv2D(64, (5,5), activation='relu'))
# model.add(Conv2D(64, (5,5), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2,2)))

# Flatten
model.add(Flatten())

# Fully connected 
model.add(Dense(128, activation='sigmoid'))
# model.add(Dense(84, activation='sigmoid'))
model.add(Dense(10, activation='softmax'))

# training model
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Training model
H = model.fit(X_train, Y_train, validation_data=(X_val, Y_val),
              batch_size=10, epochs=50, verbose=1)