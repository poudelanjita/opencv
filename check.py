import cv2
import numpy as np

# Load the images
image1 = cv2.imread('image1.png')
image2= cv2.imread('image2.png')

# Convert images to grayscale
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Detect ORB features and compute descriptors.
orb = cv2.ORB_create()
keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)

# Match features.
matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = matcher.match(descriptors1, descriptors2)

# Sort matches by distance.
matches = sorted(matches, key=lambda x: x.distance)

# Draw first 10 matches.
result = cv2.drawMatches(image1, keypoints1, image2, keypoints2, matches[:10], None)

# Show the matched image
cv2.imshow('Matched Images', result)
cv2.waitKey(0)
cv2.destroyAllWindows()