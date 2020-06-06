import cv2
import numpy as np

img = cv2.imread("HW1.png")
print(img)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('img', img)


if cv2.waitKey(0) and 0xFF==ord('q'):
    cv2.destroyAllWindows()
# for i  in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         img[i][j] = 0.299*img[i][j][0] + 0.587*img[i][j][1] + 0.114*img[i][j][2]
# #print(img_Y)
# #img_YCC = cv.cvtColor(img,cv.COLOR_RGB2YCR_CB)
# #print(img)
# #gray_img = cv.cvtColor(img_YCC,cv.COLOR_BGR2GRAY)
# cv.imwrite('output1-1.jpg',img)
# #cv.namedWindow("Image")
# #cv.imshow("Image",img)
# #cv.imshow("Image_gray",gray_img)
# #cv.waitKey(0)
# #cv.destroyAllWindows()
