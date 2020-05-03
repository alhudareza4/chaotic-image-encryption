import numpy as np 
import cv2


def generateLogisticMap(image_size):
    [row, col, dim] = image_size
    sequence_size = row * col * 8
    bit_sequence = [] #array contains 8 bits
    byte_array = []
    x1 = 0.912343121
    L = 3.99999
    xN=0
    
    for i in range(sequence_size):
        # Logistic Map Formula
        if(xN == 0):
            xN = L * x1 * (1-x1)
        else:
            xN = L * xN * (1-xN)
    
        #xN becomes the new x 
        x = xN
    
        #Convert to binary using the threshold value
        if xN <= 0.3198:
            bit = 0
        else:
            bit = 1
        #insert bit to bit_sequence
        try:
        # bit_sequence = np.append(bit_sequence, bit)
            bit_sequence.append(bit)
        except:
            bit_sequence = [bit]
        # convert to decimal
        if i % 8 == 7:
            decimal = dec(bit_sequence)
            try:
                # byte_array = np.append(byte_array, decimal)
                byte_array.append(decimal)
            except:
                byte_array = [decimal]
            bit_sequence = []
    byte_array = np.asarray(byte_array)
    logistic_map = np.reshape(byte_array, [row, col])
    return logistic_map

def dec(bitSequence):
    decimal = 0
    for bit in bitSequence:
        decimal = decimal * 2 + int(bit)
    return decimal

def generateBakerMap(image_matrix, image_size):
    