# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 15:48:06 2024

@author: amita
"""
#%%
import cv2
import tensorflow as tf
import numpy as np
#%%
# Load the trained model
model = tf.keras.models.load_model('sign_language_model.h5')

# Define labels
labels = ['hello', 'thankyou', 'yes', 'no']
#%%
# Start the webcam
cap = cv2.VideoCapture(0)
#%%
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Resize the frame to 224x224 as required by the model
    img = cv2.resize(frame, (224, 224))
    
    # Preprocess the image for the model
    img_array = np.expand_dims(img, axis=0) / 255.0
    
    # Make prediction
    predictions = model.predict(img_array)
    predicted_label = labels[np.argmax(predictions)]
    
    # Display the prediction on the frame
    cv2.putText(frame, predicted_label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
    # Show the frame
    cv2.imshow('frame', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#%%
# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
#%%
# Load the test dataset
test_dataset = image_dataset_from_directory('data/test', 
                                            image_size=(224, 224), 
                                            batch_size=32)
#%%
# Evaluate the model on the test dataset
test_loss, test_acc = model.evaluate(test_dataset)

print(f"Test Accuracy: {test_acc*100:.2f}%")

