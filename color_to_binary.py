import cv2

path = '/Users/babalia/Desktop/住房合同/signature.jpeg'
signature = cv2.imread(path)
cv2.imshow('sigature',signature)

# Binary
ret,thresh = cv2.threshold(signature,100,255,cv2.THRESH_BINARY)
print('ret',ret)
cv2.imshow('sigature_binary',thresh)
cv2.imwrite('/Users/babalia/Desktop/住房合同/signature_binary.jpeg',thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()