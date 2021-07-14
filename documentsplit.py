import cv2
import numpy as np
import os
from random import shuffle
from tqdm import tqdm

train_data = 'C:/Users/eliza/Desktop/sample_data/images'
test_data = 'C:/Users/eliza/Desktop/sample_data/imagestest'
from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale = 1./255,
shear_range = 0.2,
zoom_range = 0.2,
horizontal_flip = True)
test_datagen = ImageDataGenerator(rescale = 1./255)
training_set = train_datagen.flow_from_directory(train_data,
target_size = (128, 128),
batch_size = 32,
class_mode = 'binary')
test_set = test_datagen.flow_from_directory(test_data,
target_size = (128, 128),
batch_size = 32,
class_mode = 'binary')

#def one_hot_label(img):
 #   label = img.split('.')[0]
  #  if label == 'last':
   #     ohl = np.array([1.0])
    #else:
    #    ohl = np.array([0,1])
    #return ohl

#def train_data_with_label():
#    train_images = []
 #   for i in tqdm(os.listdir(train_data)):
  #      path = os.path.join(train_data, i)
   #     img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    #    img = cv2.resize(img, (64, 64))
     #   train_images.append([np.array(img), one_hot_label(i)])
#    shuffle(train_images)
 #   return train_images

#def test_data_with_label():
 #   test_images = []
  #     path = os.path.join(test_data, i)
   #     img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    #    img = cv2.resize(img, (64, 64))
     #   test_images.append([np.array(img), one_hot_label(i)])
 #   return test_images

from keras.models import Sequential
from keras.layers import *
from keras import optimizers

#training_images = train_data_with_label()
#testing_images = test_data_with_label()

#tr_img_data = np.array([i[0] for i in training_images]).reshape(-1, 64, 64, 1)
#tr_lbl_data = np.array([i[1] for i in training_images])

#tst_img_data = np.array([i[0] for i in testing_images]).reshape(-1, 64, 64, 1)
#tst_lbl_data = np.array([i[1] for i in testing_images])

model = Sequential()

model.add(Conv2D(32, (1, 1), input_shape = (128, 128, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Flatten())
model.add(Dense(units = 256, activation = 'relu'))
model.add(Dense(units = 128, activation = 'relu'))
model.add(Dense(units = 1, activation = 'sigmoid'))
optimizers.Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
#model.fit(x = tr_img_data, y = tr_lbl_data, epochs = 12, batch_size = 100)
model.fit_generator(training_set,
steps_per_epoch = 116,
epochs = 25,
validation_data = test_set,
validation_steps = 26)
model.summary()