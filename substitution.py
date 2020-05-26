import generateTransformationMatrix as gtm
import numpy as np 
import cv2

def pixelManipulation(image_matrix, image_size):
    [row, col, dim]= image_size
    print("Image size:", image_size)

    # generate Triangular Map
    triangular_map = gtm.generateTriangularMap(image_matrix, image_size)
    print("triangular Map size:", triangular_map.shape)

    return triangular_map