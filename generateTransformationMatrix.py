import numpy as np 
import cv2
import math

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

def generateTriangularMap(image_matrix, image_size):
    # triangular map encryption
    a =-1 
    d =-1
    c = 3
    iteration = 10

    width, height, dim = image_size

    if a == -1 and d == -1:
        a = coprime(width)
        d = coprime(height)

    
    N = image_size[0]
    triangular_map = np.zeros([N,N,3], np.uint8)

    for iter in range(iteration):
        
        for x in range(width):
            for y in range(height):
                x1 = (a*x + c*y) % width
                y1 = (d*y) % height
                triangular_map[x1, y1] = image_matrix[x, y]
    
    return triangular_map

def coprime(m):

    found = 0
    for x in range(2,m):
        if math.gcd(x,m) == 1:
            return x

    return 1
    
def degenerateTriangularMap(image_matrix, image_size):
    a =-1 
    d =-1
    c =3
    iteration = 1

    width, height, dim = image_size
    N = image_size[0]
    encrypted = np.zeros([N,N,3], np.uint8)

    if a == -1 and d == -1:
        a = coprime(width)
        d = coprime(height)

    ia = imodule(a, width)
    id = imodule(d, height)

    for iter in range(iteration):
        
        for x in range(width):
            for y in range(height):
                y1 = (id*y) % height
                x1 = (ia*(x + (math.ceil(c*height/width)*width) - (c * y1))) % width
                encrypted[x1, y1] = image_matrix[x, y]
    return encrypted
def imodule(a, m):
    if m == 0: return 0
    a = a % m
    for x in range(m):
        if (a * x) % m == 1:
            return x   
    return 1