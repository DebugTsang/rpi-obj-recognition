import cv2

video_capture = cv2.VideoCapture(0)
cv2.__version__
video_capture.set(3,640)
video_capture.set(4,480)
while True:
	result, video_frame = video_capture.read()  # read frames from the video
	if result is False:
		break  # terminate the loop if the frame is not read successfully

	cv2.imshow(
		"USB Camera Test", video_frame
	)

	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

video_capture.release()
cv2.destroyAllWindows()
