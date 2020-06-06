import cv2
import matplotlib.pyplot as plt

img = cv2.imread("/Users/timwuhuang/Documents/opencv/output1-1.jpg",0)
print(img.shape)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imwrite('output1-2.jpg',thresh1)
