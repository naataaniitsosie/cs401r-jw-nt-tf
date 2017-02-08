import numpy as np

def get_end_values(img, index):
    axis = np.argmax(img, index)
    max_value = np.max(axis)
    axis[axis == 0] = 999999
    min_value = np.min(axis)
    return max_value.astype(int), min_value.astype(int)


def crop(img, src):
    max_x, min_x = get_end_values(img, 0)
    max_y, min_y = get_end_values(img, 1)
    #print(max_x)
    #print(min_x)
    #print(max_y)
    #print(min_y)
    #print(img.shape)

    imgout = src[min_x:max_x, min_y:max_y]
    return imgout