import imutils
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
cap.set(3, 640) #width
cap.set(4, 200) #height
cap.set(10,60)# brigtness

# while True:
#     success, image = cap.read()
#     #image=cv.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     cv.imshow("WOW",image)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
image=cv.imread("Puzzle.jpeg")
img_canny_edge_det=cv.Canny(image,100,100)
#img_canny_edge_det=cv.resize(img_canny_edge_det,(400,400))
img_canny_edge_det=imutils.resize(img_canny_edge_det,height=400,width=400)
#cv.imshow("Canny", img_canny_edge_det)
cv.waitKey(0)
img=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("h",img)
cv.waitKey(0)
print(cv.checkChessboard(img,img.shape))
#cv.checkChessboard(img,img.shape)