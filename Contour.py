import imutils
import cv2 as cv
image=cv.imread("Puzzle.jpeg")
image=imutils.resize(image,height=400,width=400)
img=cv.Canny(image,2,10)

def get_board(img):
    contours, hierarchy = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv.contourArea(cnt)
        if area>(img.shape[0]*img.shape[1]*5/10):
            cv.drawContours(image, cnt, -1, (255, 100, 100), 3)
            print("heehaw")
        print(area)

get_board(img)
cv.imshow("sh",image)
cv.waitKey(0)
