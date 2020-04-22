import cv2

img = cv2.imread('lena.jpg')

B,G,R = img[0,0]

print(B, G, R)
print(img.shape)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray.shape)
print(gray[0,0])