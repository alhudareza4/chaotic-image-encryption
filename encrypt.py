import os
from glob import glob
from PIL import ImageTk, Image
import cv2
import resize as res
import diffusion as dif
import substitution as sub


# Locating image directory
base_skin_dir = os.path.join('..', 'Source Code')

# iterate image processing in folder
for x in glob(os.path.join(base_skin_dir, 'images', '*.jpg')):
    #specific path of image
    filepath = os.path.abspath(x) 
    #image file name
    filename = os.path.basename(x) 
    print(filename)

    #Geting image matrix
    image_matrix = cv2.imread(filepath)
    #Geting image dimension
    image_size = image_matrix.shape

    #reshape the image into square
    image_matrix = res.resize(image_matrix, image_size)
    image_size = image_matrix.shape

    #Substitution Process
    substitued_img = sub.pixelManipulation(image_matrix, image_size)
    path = os.path.join('..', 'Source Code', 'images', 'substitued')
    newFilePath = path+"\\"+filename.split('.')[0]+".png"
    cv2.imwrite(newFilePath, substitued_img)


    #Diffusion Process
    diffused_img = dif.pixelManipulation(confused_img, confused_img.shape)
    path = os.path.join('..', 'Source Code', 'images', 'encrypted')
    newFilePath = path+"\\"+filename.split('.')[0]+".png"
    cv2.imwrite(newFilePath, diffused_img)


