import os 
from glob import glob
import diffusion as dif 
import unsubstitution as unsub 
import resize as res 
import cv2
from PIL import ImageTk, Image

base_skin_dir = os.path.join('..', 'Source Code')
for x in glob(os.path.join(base_skin_dir, 'images', 'encrypted', '*.png')):
    filepath = os.path.abspath(x) #specific path of image
    filename = os.path.basename(x) #image file name
    print(filename)
    
    #Get image matrix and its dimension
    image_matrix = cv2.imread(filepath)
    image_size = image_matrix.shape

    #reshape the image into square
    image_matrix = res.resize(image_matrix, image_size)
    image_size = image_matrix.shape
    
    #begin undiffusion
    undiffused_img = dif.pixelManipulation(image_matrix, image_size)
    path = os.path.join('..', 'Source Code', 'images', 'undiffused')
    newFilePath = path+"\\"+filename.split('.')[0]+".png"
    cv2.imwrite(newFilePath, undiffused_img)

    #begin unconfusion
    unsubstitution_img = unsub.pixelManipulation(undiffused_img, undiffused_img.shape)
    path = os.path.join('..', 'Source Code', 'images', 'decrypted')
    newFilePath = path+"\\"+filename.split('.')[0]+".png"
    cv2.imwrite(newFilePath, unsubstitution_img)