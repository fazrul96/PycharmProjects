import cv2 as cv

# Reading Photo
# img = cv.imread('Photos/1.jpg')
# cv.imshow('1', img)

def rescaleFrame(frame, scale=0.75):
    # Images, Videos, Live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

# resize_image = rescaleFrame(img)
# cv.imshow('Image',resize_image)

def changeRes(width,height):
    # Live video
    capture.set(3,width)
    capture.set(4,height)

# Reading Video
capture = cv.VideoCapture('Videos/Facebook.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()