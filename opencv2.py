import cv2
import math

videoFile = "Dataset\\videos\\Test Tom and Jerry.mp4"
imagesFolder = "Dataset\Test2"
cap = cv2.VideoCapture(videoFile)
frameRate = cap.get(5) #frame rate
i=0
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        
        filename = imagesFolder + "\\" +  str(i) + ".jpg"
        # img_re = cv2.resize(frame, (int(frame.shape[1]*0.25), int(frame.shape[0]*0.25)), interpolation = cv2.INTER_AREA)
        cv2.imwrite(filename, frame)
        i=i+1
cap.release()
print ("Done!")

