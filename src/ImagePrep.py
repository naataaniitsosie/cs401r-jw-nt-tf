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



def variance_prep(img, original, num):

    #Reduce Image Size or create image pyramid
    #img = cv2.resize(img, None, fx=1/10, fy=1/10, interpolation = cv2.INTER_AREA)
    histStretch = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    img = histStretch.apply(img)

    '''# Median Filter (get rid of text, background noise).
    img = cv2.medianBlur(img, 17) #originally (img, 17)

    # Automatically threshold image into foreground, background
    img = cv2.Canny(img, 100, 105) #originally (img, 295, 300)
    #__,img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite("../output/canny" + str(num) + ".jpg", img)'''


    x_profile = img.sum(axis=0)
    y_profile = img.sum(axis=1)

    plt.plot(y_profile)
    plt.savefig("../output/profile" + str(num) + ".jpg")
    plt.clf()

    outVariance_x = ndimage.generic_filter(x_profile, np.var, size=50)
    outVariance_y = ndimage.generic_filter(y_profile, np.var, size=50)
    plt.plot(outVariance_x)
    plt.savefig("../output/VarianceProfile" + str(num) + ".jpg")
    plt.clf()

    arg_max_y = argrelextrema(outVariance_y, np.greater, order=(len(outVariance_y) // 2))
    arg_max_x = argrelextrema(outVariance_x, np.greater, order=(len(outVariance_x) // 2))

    print(arg_max_x)
    x_peaks = arg_max_x[0]
    y_peaks = arg_max_y[0]

    if len(x_peaks) == 2:   #only crop if there are two peaks
        if len(y_peaks) == 2:
            img = original[y_peaks[0]:y_peaks[1], x_peaks[0]:x_peaks[1]]
            print(num)

    # Resize image back to original
    #img = cv2.resize(img, None, fx=10, fy=10, interpolation=cv2.INTER_CUBIC)

    return img

