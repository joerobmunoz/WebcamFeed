import os.path
import cv2

def save_image(i, img):
    """Checks to see if image file name is free and saves the web cam feed"""
    fileName = "WebcamFeed_" + str(i) + ".png"
    if os.path.isfile(fileName):
        save_image(i + 1, img)
    else:
        cv2.imwrite(fileName, img)
        print 'Saved camera image: ' + "\"" + fileName + "\""
        
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("Webcam", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
    elif key == ord('s'):
		save_image(0, frame)
        
cv2.destroyWindow("Webcam")

        
