# -*- coding: utf-8 -*-
"""cnn_numberAna.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SQp5cCQuUvEb3oO5eKmUZDE6fPy_cgww
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

model = tf.keras.models.Sequential([
                                    tf.keras.layers.Conv2D(5,(3,3), activation=tf.nn.relu,input_shape=(28,28,1)), 
                                    tf.keras.layers.MaxPool2D(2,2),
                                    tf.keras.layers.Flatten(), 
                                    tf.keras.layers.Dense(10, activation=tf.nn.relu), 
                                    tf.keras.layers.Dense(10, activation=tf.nn.relu), 
                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

model.compile(optimizer = tf.optimizers.Adam(),
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

history=model.fit(training_images, training_labels, epochs=100)

plt.xlabel('epoch')
plt.title("Accuracy and loss graph")
plt.legend(['accuracy','loss'],loc='upper right')


plt.plot(history.history['accuracy'])

plt.ylabel('accuracy')
plt.ylim([0,1])
plt.twinx()

plt.plot(history.history['loss'],color='red')
plt.ylabel('loss')
plt.ylim([0,2])





plt.show()

model.evaluate(test_images, test_labels)