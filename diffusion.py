import numpy as np
import os
import matplotlib.pyplot as plt
import cv2
import generateTransformationMatrix as gtm

def pixelManipulation(image_matrix, image_size):
    [row, col, dim] = image_size
    print("Image size:",image_size)   

    # generate logistic map 
    logistic_map = gtm.generateLogisticMap(image_size)
    print("Logistic Map size:", logistic_map.shape)

    resultant_matrix = []
    image_matrix_rgb = []

    logistic_map_flatten = logistic_map.flatten()
    for i in range(3):
        image_matrix_rgb.append(image_matrix[:, :, i].flatten())


    for i in range(3):
        resultant_matrix_per_channel = []
        for j in range(logistic_map_flatten.size):
            resultant_matrix_per_channel.append(logistic_map_flatten[j] ^ image_matrix_rgb[i][j])
        resultant_matrix.append(resultant_matrix_per_channel)
    resultant_matrix = np.asarray(resultant_matrix)

    resultant_matrix_b = np.reshape(resultant_matrix[0], [row,col])
    resultant_matrix_g = np.reshape(resultant_matrix[1], [row,col])
    resultant_matrix_r = np.reshape(resultant_matrix[2], [row,col])
    resultant_matrix = np.dstack((resultant_matrix_b, resultant_matrix_g, resultant_matrix_r))
     

    return resultant_matrix