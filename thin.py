# -*- coding:utf-8 -*-

import pickle
import os
import cv2 as cv
import numpy as np
from skimage import morphology
from PIL import Image

lh = 0
lw = 0


pic_list = 'C:/Users/35472/naoqi/pic_datas'

for filename in os.listdir(pic_list):
    with open(os.path.join(pic_list, filename), 'r') as f:
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
    img_1 = img_0.astype(np.uint8) * 255
    pic_list_22 = "C:/Users/35472/naoqi/img_list"
    file_path2 = os.path.join(pic_list_22, filename + '.jpg')
    cv.imwrite(file_path2, img_1)

    # cv.imshow(filename + '1', img1)
    # cv.imshow(filename + '2', th2)
    cv.imshow(filename, img_1)

    # cv.imshow(filename, img1)

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

    im = Image.open(file_path2)
    im2 = im.convert('1')

    width, height = im2.size
    print (width, height)
    i = 0
    p = []
    pp = []
    ppp = []
    pic_list_01 = 'C:/Users/35472/naoqi/010101/'
    file_path = os.path.join(pic_list_01, filename + '.txt')
    with open(file_path, 'w') as f:
        k = []
        kh = {}
        kw = {}
        for h in range(height):
            for w in range(width):
                f.write(str(int((255 - (im2.getpixel((w, h)))) / 255)))
                if w == width - 1:
                    f.write("\n")
                if h == 120 and int((255 - (im2.getpixel((w, h)))) / 255) == 0:
                    print(w, h)
                    p.append(w)
                if h == 220 and w > 10 and int((255 - (im2.getpixel((w, h)))) / 255) == 0:
                    pp.append(w)
                if h == 30 and int((255 - (im2.getpixel((w, h)))) / 255) == 0:
                    ppp.append(w)
                if int((255 - (im2.getpixel((w, h)))) / 255) == 0:
                    # print(w, h)
                    lw = max(w, lw)
                    kh[w] = h
                    kw[h] = w
                    k.append((w, h))
                    # print("\n")
            #
            # kh[lw] = h

        cv.line(img1, ((sum(p))//(len(p)), 120), (160, 240), (255, 255, 0), 1)
        cv.imshow(filename + '3', img1)

        print (pp)
        if len(ppp) == 3:
            print (filename)
            print ('中间线为中线')
        else:
            if len(pp) == 2:
                lpp = abs(160 - pp[0])
                rpp = abs(160 - pp[1])
                print (lpp, rpp)
                if lpp > rpp:
                    print (filename)
                    print ('右线为中线')
                else:
                    print (filename)
                    print ('左线为中线')
            else:
                print (filename)
                print ('中间线为中线')
        # aa = sum(pp)//(len(pp))
    cv.waitKey(0)
    cv.destroyAllWindows()