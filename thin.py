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
    print(len(img))
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
    print(width, height)
    i = 0
    p = []
    pp = []
    ppp = []
    p4 = []
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
                if h == 35 and int((255 - (im2.getpixel((w, h)))) / 255) == 0:
                    p.append(w)
                if h == 120 and int((255 - (im2.getpixel((w, h)))) / 255) == 0:
                    print(w, h)
                    pp.append(w)
                if h == 215 and w > 10 and int((255 - (im2.getpixel((w, h)))) / 255) == 0:
                    ppp.append(w)
                if h == 55 and int((255 - (im2.getpixel((w, h)))) / 255) == 0:
                    p4.append(w)
                if int((255 - (im2.getpixel((w, h)))) / 255) == 0:
                    # print(w, h)
                    lw = max(w, lw)
                    kh[w] = h
                    kw[h] = w
                    k.append((w, h))
                    # print("\n")
            #
            # kh[lw] = h

        #
        # # cv.line(img1, ((sum(p))//(len(p)), 120), (160, 240), (255, 255, 0), 1)
        #
        # cv.line(img1, ((sum(p))//(len(p)), 120), ((sum(ppp))//(len(ppp)), 0), (255, 255, 0), 1)
        # cv.line(img1, ((sum(p))//(len(p)), 120), ((sum(pp))//(len(pp)), 240), (255, 255, 0), 1)
        # # cv.line(img1, ((sum(p))//(len(p)), 120), (160, 240), (255, 255, 0), 1)
        print("fghjkjhgfd")
        print(p4)
        print("fghjkjhgfd")
        # if len(ppp) == 1 and len(pp) == 2 and pp[0] <= 90:
        #     cv.line(img1, (85, 120), (80, 0), (255, 255, 0), 1)
        #     cv.line(img1, (85, 120), (160, 240), (255, 255, 0), 1)
        #
        # else:
        if len(p4) == 3:
            cv.line(img1, (85, 120), (80, 0), (255, 255, 0), 1)
            cv.line(img1, (85, 120), (160, 240), (255, 255, 0), 1)
        else:
            if len(p) == 3 or len(pp) == 3 or len(ppp) == 3:
                cv.line(img1, ((sum(pp)) // (len(pp)), 120), (80, 0), (255, 255, 0), 1)  #
                cv.line(img1, ((sum(pp)) // (len(pp)), 120), (160, 240), (255, 255, 0), 1)
            # elif len(p) == 2 and len(ppp) == 2 and len(pp) != 3 and p[0] <= 100 and ppp[1] >= 265:
            #     cv.line(img1, (85, 120), (80, 0), (255, 255, 0), 1)
            #     cv.line(img1, (85, 120), (160, 240), (255, 255, 0), 1)
            elif len(p) == 2:
                cv.line(img1, ((sum(pp)) // (len(pp)), 120), ((sum(p)) // (len(p)), 0), (255, 255, 0), 1)
                if len(ppp) == 2:
                    cv.line(img1, ((sum(pp)) // (len(pp)), 120), (160, 240), (255, 255, 0), 1)
                elif len(ppp) == 1:
                    cv.line(img1, ((sum(pp)) // (len(pp)), 120), (160, 240), (255, 255, 0), 1)
                else:
                    if pp[0] <= 90:
                        cv.line(img1, ((sum(pp)) // (len(pp)), 120), (160, 240), (255, 255, 0), 1)
                    else:
                        cv.line(img1, ((sum(pp)) // (len(pp)), 120), (240, 240), (255, 255, 0), 1)

        pic_list_33 = "C:/Users/35472/naoqi/img_line_list"
        file_path33 = os.path.join(pic_list_33, filename + '.jpg')
        cv.imwrite(file_path33, img1)

        # cv.line(img1, ((sum(p))//(len(p)), 120), (160, 240), (255, 255, 0), 1)
        cv.imshow(filename + '3', img1)

        print(ppp)

        if len(p) == 3:
            print(filename)
            print('中间线为中线')
        else:
            if len(ppp) == 2:
                lppp = abs(160 - ppp[0])
                rppp = abs(160 - ppp[1])
                print(lppp, rppp)
                if lppp > rppp:
                    print(filename)
                    print('右线为中线')
                else:
                    print(filename)
                    print('左线为中线')
            else:
                print(filename)
                print('中间线为中线')
        # aa = sum(pp)//(len(pp))
    cv.waitKey(0)
    cv.destroyAllWindows()
