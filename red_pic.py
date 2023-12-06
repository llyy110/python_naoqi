# -*- coding:utf-8 -*-

import pickle
import os
import cv2 as cv
import numpy as np
from skimage import morphology
from PIL import Image

pic_list = 'C:/Users/35472/naoqi/pic_datas'

for filename in os.listdir(pic_list):
    with open(os.path.join(pic_list, filename), 'r') as f:
        l = pickle.load(f)
    m = l[6]
    img = np.frombuffer(m, dtype=np.uint8)
    print (len(img))
    img1 = img.reshape(240, 320)
    cv.imshow(filename + '1', img1)
    img_zhong = cv.medianBlur(img1, 19)
    shuang = cv.bilateralFilter(img_zhong, d=0, sigmaColor=30, sigmaSpace=20)

    th2 = cv.adaptiveThreshold(shuang, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 31, 25)
    # imgf = cv.erode(th2, (5, 5))
    # imgp = cv.dilate(imgf, (5, 17))
    # imgf[imgf == 0] = 1
    # imgf[imgf == 255] = 0
    # img_0 = morphology.skeletonize(imgf)
    # img_1 = img_0.astype(np.uint8) * 255
    # pic_list_22 = "C:/Users/35472/naoqi/img_list"
    # file_path2 = os.path.join(pic_list_22, filename + '.jpg')
    # cv.imwrite(file_path2, img_1)
    # cv.imshow(filename, img_1)
    # cv.imshow(filename, img1)

    cv.imshow(filename, th2)
    # color = img_1[240]
    # white_count = np.sum(color == 0)
    # white_count_judge = np.sum(color == 255)
    # if white_count_judge == 640:
    #     print "黑色的像素点为0"
    #     pass
    # else:
    #     white_index = np.where(color == 0)
    #     if white_count == 0:
    #         white_count = 1
    #     center = (white_index[0][white_count - 1] + white_index[0][0]) / 2
    #     direction = center - 120
    #     print(direction)

    cv.waitKey(0)
    cv.destroyAllWindows()
    #
    # im = Image.open(file_path2)
    # im2 = im.convert('1')
    #
    # w, h = im2.size
    # print (w, h)
    # i = 0
    # pic_list_01 = 'C:/Users/35472/naoqi/010101/'
    # file_path = os.path.join(pic_list_01, filename + '.txt')
    # with open(file_path, 'w') as f:
    #     for c in range(h):
    #         for j in range(w):
    #             f.write(str(int((255 - (im2.getpixel((j, c)))) / 255)))
    #             if j == w - 1:
    #                 f.write("\n")
    #
    # with open(file_path, 'r') as f:
    #     for k in f.readlines():
    #         if k == 1:
    #             print('stop')




