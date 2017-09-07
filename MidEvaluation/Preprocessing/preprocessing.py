import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
from skimage.io import imread

png_image = Image.open("C:\\Users\\Shubhi\\Desktop\\Minor\\d.png").convert('LA');
png_image.save("C:\\Users\Shubhi\\Desktop\\Minor\\greyscale.png")
png_img=imread("C:\\Users\\Shubhi\\Desktop\\Minor\\greyscale.png")

print png_img #//printing the numpy image array
#myImage.show();
#img = cv2.imread("C:\\Users\\Shubhi\\Desktop\\Minor\\greyscale.png")
##JPEG IMAGE

jpg_image = Image.open("C:\\Users\\Shubhi\\Desktop\\Minor\\colortest.jpg").convert('L');
jpg_image.save("C:\\Users\Shubhi\\Desktop\\Minor\\colorjpg.jpg")
jpg_img=imread("C:\\Users\\Shubhi\\Desktop\\Minor\\colorjpg.jpg")


dst = cv2.fastNlMeansDenoisingColored(png_img,None,10,10,7,10)
plt.subplot(121),plt.imshow(png_img)
plt.subplot(122),plt.imshow(dst)
#plt.show()


png_img = cv2.imread("C:\\Users\\Shubhi\\Desktop\\Minor\\greyscale.png",0)

ret,th = cv2.threshold(png_img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(png_img,(5,5),0)
plt.subplot(3,3,4),plt.imshow(png_img,'gray')
plt.title("Noise removed image"), plt.xticks([]), plt.yticks([])

plt.subplot(3,3,6),plt.imshow(th,'gray')
plt.title("Ostu Thresholding"), plt.xticks([]), plt.yticks([])

#plt.show()
edges = cv2.Canny(th,100,200) 
#plt.subplot(121),plt.imshow(th,cmap = 'gray')
#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Detected Image Image'), plt.xticks([]), plt.yticks([]) 
plt.show()

