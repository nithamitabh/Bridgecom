# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 15:42:25 2024

@author: amita
"""
#%%
import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory
#%%
# Load the dataset from your labeled folders
train_dataset = image_dataset_from_directory("Tensorflow/workspace/images/collectedimages", 
                                             image_size=(224, 224), 
                                             batch_size=32, 
                                             subset="training", 
                                             validation_split=0.2,
                                             seed=123)

val_dataset = image_dataset_from_directory("Tensorflow/workspace/images/collectedimages", 
                                           image_size=(224, 224), 
                                           batch_size=32, 
                                           subset="validation", 
                                           validation_split=0.2,
                                           seed=123)

#%%
# Create a basic CNN model
model = tf.keras.Sequential([
    tf.keras.layers.Rescaling(1./255, input_shape=(224, 224, 3)),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(len(train_dataset.class_names), activation='softmax')  # Number of classes based on your labels
])
#%%
# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#%%
# Train the model
model.fit(train_dataset, validation_data=val_dataset, epochs=5)
#%%
# Save the model for later use
model.save('sign_language_model.h5')
