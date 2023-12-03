import pickle
import cv2 as cv
import numpy as np
from skimage import morphology
from PIL import Image

path_pic = r'C:/Users/35472/naoqi/pic_datas/100.dat'

with open(path_pic, 'r')as f:

    l = pickle.load(f)
m = l[6]
img = np.frombuffer(m, dtype=np.uint8)
print (len(img))
img1 = img.reshape(240, 320)
img_zhong = cv.medianBlur(img1, 19)
shuang = cv.bilateralFilter(img_zhong, d=0, sigmaColor=30, sigmaSpace=20)
th2 = cv.adaptiveThreshold(shuang, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 31, 25)
imgf = cv.erode(th2, (5, 5))
imgp = cv.dilate(imgf, (5, 17))
imgf[imgf == 0] = 1
imgf[imgf == 255] = 0
img_0 = morphology.skeletonize(imgf)
img_1 = img_0.astype(np.uint8)*255
cv.imwrite('xihua.png', img_1)
cv.imshow('13131', img_1)

cv.waitKey(0)
cv.destroyAllWindows()

im = Image.open('xihua.png')
im2 = im.convert("1")

w, h = im2.size
print (w, h)

with open('xihua.txt', "w") as f:
    for c in range(h):
        for j in range(w):
            f.write(str(int((255 - (im2.getpixel((j, c)))) / 255)))
            if j == w - 1:
                f.write("\n")

#