import generateTransformationMatrix as gtm 
import numpy as np 
import cv2

def pixelManipulation(image_matrix, image_size):
    [row, col, dim] image_size
    print("Image size:", image_size)

    # generate Baker's Map
    baker_map = gtm.generateBakerMap(image_matrix, image_size)
    print("Bakers map size:", baker_map.shape)

    return baker_map