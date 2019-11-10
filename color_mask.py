import cv2
import numpy as np

path = '/Users/babalia/Desktop/住房合同/signature.jpeg'
signature = cv2.imread(path)
cv2.imshow('sigature',signature)

# 转化为HSV
name_hsv = cv2.cvtColor(signature, cv2.COLOR_BGR2HSV)
# 获取mask
lower_blue=np.array([0,0,0])
upper_blue=np.array([180,255,80])
# mask 为单通道
mask = cv2.inRange(name_hsv, lower_blue, upper_blue)
# 最大图像灰度值减去原图像，即可得到反转的图像
dst = 255 - mask
cv2.imshow('Mask', dst)
#cv2.imshow('Mask', name_rgb)



cv2.waitKey(0)
cv2.destroyAllWindows()