import cv2
import numpy as np

img = cv2.imread('output1-2.jpg', 0)
img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]  # ensure binary
ret, labels = cv2.connectedComponents(img)

# Map component labels to hue val
label_hue = np.uint8(250*labels/np.max(labels))
blank_ch = 255*np.ones_like(label_hue)
labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

# cvt to BGR for display
labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2RGB)

# set bg label to black
labeled_img[label_hue==0] = 0
#select car number 
for i in range(labeled_img.shape[0]):
    for j in range(labeled_img.shape[1]):
        if(j > 330 and j < 395 and i >230 and i<270):
            if (labeled_img[i][j][0] == 255 and labeled_img[i][j][1] == 110 and labeled_img[i][j][2] == 0):
                labeled_img[i][j] = [255,255,255]
            elif(labeled_img[i][j][1] > 110 and labeled_img[i][j][1] != 204):
                labeled_img[i][j] = [255,255,255]  
            else:
                labeled_img[i][j] = [0,0,0]
        else:
            labeled_img[i][j] = [0,0,0]
img_IOA = labeled_img[230:270,330:395]
cv2.imwrite('output1-4.jpg', img_IOA)
cv2.imshow('img', img_IOA)
cv2.waitKey()
