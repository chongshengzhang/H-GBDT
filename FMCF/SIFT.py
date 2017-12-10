import cv2

gray = cv2.imread("../images/BioID_0000.pgm")


detector = cv2.SIFT()
keypoints = detector.detect(gray, None)
img = cv2.drawKeypoints(gray, keypoints)
# print (keypoints[0].x)
#img = cv2.drawKeypoints(gray,keypoints,flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('test', img);
cv2.waitKey(0)
cv2.destroyAllWindows()



