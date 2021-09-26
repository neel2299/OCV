import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
cap.set(3, 640) #width
cap.set(4, 200) #height
cap.set(10,60)# brigtness
success, image = cap.read()
def empty(something):
    pass

# cv.namedWindow("Track")
# cv.createTrackbar("Hue min","Track",0,255,empty)
# cv.createTrackbar("Hue max","Track",0,255,empty)
# cv.createTrackbar("Sat min","Track",0,255,empty)
# cv.createTrackbar("Sat max","Track",0,255,empty)
# cv.createTrackbar("Val min","Track",0,255,empty)
# cv.createTrackbar("Val max","Track",0,255,empty)
pen=[88,205,0,153,205,255]
def contours(ima):
    contours, hierarchy = cv.findContours(ima, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 100:
            cv.drawContours(img, cnt, -1, (255, 100, 100), 3)
            peri=cv.arcLength(cnt,True)
            approx=cv.approxPolyDP(cnt,0.02*peri,False)
            x,y,w,h=cv.boundingRect(approx)
    return (x+w//2,y)
def draw(point):
    for point in points:
        cv.circle(result,(point[0],point[1]),10,(255,0,0),cv.FILLED)
points=[]
result=np.copy(image)
result.fill(0)
while True:
    # h_min=cv.getTrackbarPos("Hue min","Track")
    # h_max = cv.getTrackbarPos("Hue max", "Track")
    # s_min = cv.getTrackbarPos("Sat min", "Track")
    # s_max = cv.getTrackbarPos("Sat max", "Track")
    # v_min = cv.getTrackbarPos("Val min", "Track")
    # v_max = cv.getTrackbarPos("Val max", "Track")
    lower=np.array([88,0,205])
    upper=np.array([205,153,255])
    success, image = cap.read()
    image=cv.flip(image,1)
    img=image#cv.cvtColor(image,cv.RGB)
    #for values Rm=88 RM=205 Bm=0 BM=153 Gm=205 GM=255
    mask=cv.inRange(img,lower,upper)

    x,y=contours(mask)

    cv.circle(result,(x, y), 10, (255, 0, 0), cv.FILLED)
    if x!=0 or y!=0:
        points.append([x,y])
    #image=cv.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv.imshow("WOW",image)
    cv.imshow("WOW2", img)
    cv.imshow("WOW1",result)
    #cv.imshow("WOW3", mask)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


