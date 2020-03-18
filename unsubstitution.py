import numpy as np 
import cv2
import generateTransformationMatrix as gtm 

def pixelManipulation(image_matrix, image_size):
    [row, col, dim] = image_size
    print("image size:", image_size)

    baker_map = gtm.reconstructBakerMap(image_matrix, image_size)
    print("Baker Map size:", baker_map.shape)

    return baker_map