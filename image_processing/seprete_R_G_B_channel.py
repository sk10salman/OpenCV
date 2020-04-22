import cv2

img = cv2.imread('lena.jpg')

#Split function splits the image into each color index

B,G,R = cv2.split(img)

cv2.imshow('RGB Image', img)

cv2.imshow('Red Channel ', R)
cv2.imshow('Green Channel ', G)
cv2.imshow('Blue Channel ', B)

cv2.waitKey(0)
cv2.destroyAllWindows()


# Let's remake the original image
merged = cv2.merge([B, G, R])
cv2.imshow('Merged', merged)


#Lets apply the blue color

merged1 = cv2.merge([B+100, G, R])
cv2.imshow('Merged with Blue', merged1)

cv2.waitKey(0)
cv2.destroyAllWindows()

