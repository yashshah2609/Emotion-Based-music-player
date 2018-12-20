import cv2
video_capture=cv2.VideoCapture(0)
def nolight():
	return video_capture.read()