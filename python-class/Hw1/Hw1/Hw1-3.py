import cv2
import numpy as np

img = cv2.imread('output1-2.jpg', 0)
img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]  # ensure binary
ret, labels = cv2.connectedComponents(img)

# Map component labels to hue val
label_hue = np.uint8(250*labels/np.max(labels))
blank_ch = 255*np.ones_like(label_hue)
labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

# cvt to RGB for display
labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2RGB)

# set bg label to black
labeled_img[label_hue==0] = 0

#img_size = labeled_img.shape
cv2.imwrite('output1-3.jpg',labeled_img)
cv2.imshow('test.png', labeled_img)
            
#cv2.imwrite('test.png', labels*255)
cv2.waitKey()
