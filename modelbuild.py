from __future__ import print_function

import os
import numpy as np
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding
from keras.layers import LSTM
from keras.datasets import imdb

max_features = 20000
# cut texts after this number of words (among top max_features most common words)
maxlen = 80
batch_size = 16

embeddings_index = {}
with open(os.path.join('glove.6B.300d.txt'), encoding="utf8") as f:
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = coefs

print('Loading data...')
#loads data from a data set of 50000 movie reviews of varying length
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
#divides the data into training set and testing set
print(len(x_train), 'train sequences')
print(len(x_test), 'test sequences')

print('Pad sequences (samples x time)')
#truncates and pads the input sequences so they are all the same length
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)

print('Build model...')
model = Sequential()
#first layer with vectors to represent each word
model.add(Embedding(max_features, 128))
#adds another layer of memory units
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
#output layer with one neuron and a sigmoid activation function to make prediction 0 or 1 (good or bad)
model.add(Dense(1, activation='sigmoid'))

# try using different optimizers and different optimizer configs
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('Train...')

model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=200,
          validation_data=(x_test, y_test))
#final evaluation of the model and records the score and accuracy
score, acc = model.evaluate(x_test, y_test,
                            batch_size=batch_size)
print('Test score:', score)
print('Test accuracy:', acc)