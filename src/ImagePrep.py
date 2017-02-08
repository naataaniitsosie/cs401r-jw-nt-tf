import cv2

def prep(img):

    #Reduce Image Size or create image pyramid
    img = cv2.resize(img, None, fx=1/10, fy=1/10, interpolation = cv2.INTER_AREA)

    # Histogram Stretch Image
    histStretch = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    img = histStretch.apply(img)

    # Median Filter (get rid of text, background noise).
    img = cv2.medianBlur(img, 17)

    # Automatically threshold image into foreground, background
    img = cv2.Canny(img, 295, 300)
    #__,img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # Resize image back to original
    img = cv2.resize(img, None, fx=10, fy=10, interpolation=cv2.INTER_CUBIC)

    return img