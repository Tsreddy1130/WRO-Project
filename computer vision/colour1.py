import cv2

red =cv2.imread(r'C:\Users\SESHIREDDY\Documents\WRO\red.png',1)
green =cv2.imread(r'C:\Users\SESHIREDDY\Documents\WRO\green.png',1)
blue = cv2.imread(r'C:\Users\SESHIREDDY\Documents\WRO\blue.png',1)
test = cv2.imread(r'C:\Users\SESHIREDDY\Documents\WRO\test1.png',1)

cv2.imshow('image',red)
cv2.imshow('green',green)
cv2.imshow('blue',blue)
#cv2.waitKey(9999)

pixel = red[50,50]
print(pixel)
pixel2 = green[50,50]
print(pixel2)

pixel3 =blue[50,50]
print(pixel3)

print(test[100,100])