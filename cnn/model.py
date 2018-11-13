import keras
from keras.models import Sequential
from keras.layers.core import Flatten, Dense, Dropout
from keras.layers.convolutional import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras.optimizers import SGD, Adam, Adamax
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.convolutional import Conv2D, MaxPooling2D
import cv2
import numpy as np
import h5py

#'vgg16_weights.h5''vgg16_weights.h5'

model = Sequential()

# First convolutional layer with max pooling
model.add(Conv2D(20, (5, 5), padding="same", input_shape=(20, 20, 1), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

# Second convolutional layer with max pooling
model.add(Conv2D(50, (5, 5), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

# Hidden layer with 500 nodes
model.add(Flatten())
model.add(Dense(500, activation="relu"))

# Output layer with 32 nodes (one for each possible letter/number we predict)
model.add(Dense(32, activation="softmax"))



for layer in model.layers:
    layer.trainable = False


model.summary()
#new_model.load_weights('my_model_weights.h5')



train_datagen = ImageDataGenerator(
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator()
                                  
nb_train_samples = 1202
nb_validation_samples = 771
epochs = 1
batch_size = 8

train_generator = train_datagen.flow_from_directory(
        'image2',  
        batch_size=batch_size,
        shuffle=True,
        target_size=(20,20),
        class_mode='categorical')  



model.compile(loss='categorical_crossentropy',
              optimizer=Adam(lr=0.005, beta_1=0.9, beta_2=0.999, epsilon=None, decay=1e-9, amsgrad=False),
              metrics=['accuracy'])




model.save_weights('my_model_weights2.h5')


