import cv2 as cv

# Reading Photo
img = cv.imread('Photos/1.jpg')
cv.imshow('1',img)
cv.waitKey(0)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width,height)
# Reading Video
# capture = cv.VideoCapture('Videos/1.jpg')
#
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video',frame)
#
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
#
# capture.release()
# cv.destroyAllWindows()

