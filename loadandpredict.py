import tensorflow as tf 
import sklearn 
import numpy as np 
import matplotlib.pyplot as plt
import os
from keras.preprocessing import image
import cv2

def create_cnn_model():  

    model=tf.keras.models.Sequential() #if imported from tensorflow.keras import models we would write models.Sequential
    
    model.add(tf.keras.layers.Conv2D(64,(3,3),activation='relu',input_shape=(32,32,3)))
    model.add(tf.keras.layers.MaxPool2D((2,2)))
    model.add(tf.keras.layers.Conv2D(64,(3,3),activation='relu'))
    model.add(tf.keras.layers.MaxPool2D((2,2)))
    model.add(tf.keras.layers.Conv2D(128,(3,3),activation='relu'))
    model.add(tf.keras.layers.Conv2D(64,(3,3),activation='relu'))

    
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(64,activation='relu'))
    model.add(tf.keras.layers.Dense(128,activation='relu'))
    model.add(tf.keras.layers.Dense(64,activation='relu'))
    model.add(tf.keras.layers.Dense(10,activation='softmax'))
    
    # opt = tf.keras.optimizers.Adam(learning_rate=0.0001)
    model.compile(optimizer=tf.keras.optimizers.Adam(),loss='categorical_crossentropy',metrics=['accuracy'])
    return model

def loadModel():
    Loaded_model=create_cnn_model()
    Loaded_model.load_weights('./model/model.h5')
    Loaded_model.summary()
    return Loaded_model

def openImage():
    base_dir='./uploadedImages'
    image=os.listdir(base_dir)
    print(image)
    img = tf.keras.preprocessing.image.load_img(os.path.join(base_dir,image[0]),target_size=(32, 32))
    input_arr = tf.keras.preprocessing.image.img_to_array(img)
    input_arr = np.array([input_arr])  # Convert single image to a batch.
    return input_arr

def predict():    
    labels=['airplane','automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
    try:
        model=loadModel()
        # print('Yee, I am working')
        # print(model.summary())
        return (labels[np.argmax(model.predict(openImage()))])
    except Exception as e:
        print('Error occured',e)



if __name__=='main':
    print('I am main module now')
    pass
