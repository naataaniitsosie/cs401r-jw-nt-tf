import sys
import src.ImagePrep as imgp
import src.Crop as Crop
import cv2
import src.OpenCVImg as SecCrop

def CropTopImage(src):

    # prepare image
    original = cv2.imread(src, 0)
    imgout = imgp.prep(original)

    #crop
    imgout = Crop.crop(imgout, original)
    
    imgout = imgp.variance_prep(imgout, original, num)

    return imgout


img = "../images/Crop1.jpg"
result_img = CropTopImage(img)
cv2.imwrite("../first_crop/result1.jpg", result_img)
SecCrop.openCVPrep(result_img, "1")

img = "../images/Crop2.jpg"
result_img = CropTopImage(img)
cv2.imwrite("../first_crop/result2.jpg", result_img)
SecCrop.openCVPrep(result_img, "2")

img = "../images/Crop3.jpg"
result_img = CropTopImage(img)
cv2.imwrite("../first_crop/result3.jpg", result_img)
SecCrop.openCVPrep(result_img, "3")

img = "../images/Crop4.jpg"
result_img = CropTopImage(img)
cv2.imwrite("../first_crop/result4.jpg", result_img)
SecCrop.openCVPrep(result_img, "4")

img = "../images/Crop5.jpg"
result_img = CropTopImage(img)
cv2.imwrite("../first_crop/result5.jpg", result_img)

img = "../images/Crop6.jpg"
result_img = CropTopImage(img)
cv2.imwrite("../first_crop/result6.jpg", result_img)

img = "../images/Crop7.jpg"
result_img = CropTopImage(img)
cv2.imwrite("../first_crop/result7.jpg", result_img)

img = "../images/Crop8.jpg"
result_img = CropTopImage(img)
cv2.imwrite("../first_crop/result8.jpg", result_img)

img = "../images/Crop9.jpg"
result_img = CropTopImage(img)
cv2.imwrite("../first_crop/result9.jpg", result_img)

img = "../images/Crop10.jpg"
result_img = CropTopImage(img)
cv2.imwrite("../first_crop/result10.jpg", result_img)

img = "../images/Crop11.jpg"
result_img = CropTopImage(img)
cv2.imwrite("../first_crop/result11.jpg", result_img)
