import numpy as np 
import cv2
import generateTransformationMatrix as gtm 

def pixelManipulation(image_matrix, image_size):
    [row, col, dim] = image_size
    print("image size:", image_size)

    triangular_map = gtm.degenerateTriangularMap(image_matrix, image_size)
    print("triangular_map size:", triangular_map.shape)

    return triangular_map