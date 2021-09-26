import cv2 as cv
#One proj can be making a bot that behaves like a human
#build a chrome extension to highlight all the same words when you select one
import numpy as np
img = cv.imread("Puzzle.jpeg")
#curveness of pieces at different heights
def image_to_matrix(img):
    dx=img.shape[0]//8
    dy=img.shape[1]//8
    mat=[]
    for i in range(0,8):
        lis=[]
        for j in range(0,8):
            points1 = np.float32([[i*dx,j*dy],[(i+1)*dx,j*dy],[i*dx,(j+1)*dy],[(i+1)*dx,(j+1)*dy]])
            points2 = np.float32([[0,0], [dx,0], [0,dy], [dx,dy]])
            #points2 = np.float32([[i*dx,j*dy],[(i+1)*dx,j*dy],[i*dx,(j+1)*dy],[(i+1)*dx,(j+1)*dy]])
            matrix=cv.getPerspectiveTransform(points1, points2)
            output=cv.warpPerspective(img,matrix,(dx,dy))
            lis.append(output)
            cv.imshow(str(i)+str(j), output)
        mat.append(lis)

    return mat

dummy= image_to_matrix(img)
cv.imshow("first block",dummy[7][6])
cv.waitKey(0)