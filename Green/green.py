import cv2
import numpy as np

for i in range(1, 4):
    img = cv2.imread('green0' + str(i) + '.png', 1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_api0 = np.array([50, 100, 100])
    upper_api0 = np.array([70, 255, 255])
    mask = cv2.inRange(hsv, lower_api0, upper_api0)

    new_img = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("hasil" + str(i) + ".png", new_img)
    cv2.imshow('image', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
