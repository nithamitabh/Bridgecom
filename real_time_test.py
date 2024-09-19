#%%
import cv2
import os
import time
import uuid
#%%
labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
num_imgs = 15
#%%
IMAGE_PATH = 'Tensorflow/workspace/images/collectedimages'

#%%
for label in labels:
    # Create the folder if it doesn't exist
    os.makedirs(os.path.join(IMAGE_PATH, label), exist_ok=True)
    
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    
    for imgnum in range(num_imgs):
        ret, frame = cap.read()
        
        if not ret:
            print("Failed to capture image")
            break
        
        imgname = os.path.join(IMAGE_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        
        time.sleep(3)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
#%%

