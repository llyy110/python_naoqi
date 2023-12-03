# -*- coding: utf-8 -*-
# !/usr/bin/env python2
# @author 王占泽
# @date 2021/5/19
from naoqi import ALProxy
import vision_definitions

import os
import time
import random
import pickle

"""
这个文件是py2.7版本的, 用于获取相机容器, 并保存到本地, 用于测试
"""

start = time.clock()  # 用于时间测试
rand = random.randint(0, 20)  # 随机字符串, 用于订阅相机

ov7725_w = 320  # 图片宽度
ov7725_H = 240  # 图片高度
# row_start = 229  # 从后往前扫描的位置
# row_end = 110  # 从后往前扫描的结束位置
Middle_H = 119  # 垂直中点
Middle_W = 159  # 水平中点
Start = 20
End = 209
BLACK = 0
WHITE = 1
THRESHOLDING = 90  # 二值化处理阈值


class ClassName:
    def __init__(self, _ip, _port, camera_id, _tts):
        self._cameraID = camera_id  # 订阅的相机编号, # 1下摄像头，0上摄像头
        self._resolution = vision_definitions.kQVGA  # 320 * 240
        self._colorSpace = vision_definitions.kYuvColorSpace  # 使用 Yuv 颜色空间,Y为亮度分量,调用相机后返回容器内[6]为各像素亮度值
        self._fps = 30  # 帧率,对处理速度影响不大
        self._imgClient = ""
        self.data1 = []
        self.num_image = []
        self.data = []
        self._imgData = None
        self.length = 0
        self.image_dec = []
        self.DataLine = []
        self._tts = _tts
        self.t = 0
        self.ty = 0
        self._register_image_client(IP, PORT)  # 订阅相机
        self.img_file_num = 0

    # 订阅相机
    def _register_image_client(self, _ip, _port):
        """ [0]：宽度  [1]：高度  [2]：层数  [3]：ColorSpace  [4]：qi :: Clock的时间戳（秒）  [5]：qi :: Clock的时间戳（微秒）
            [6]：大小为高度*宽度*层数的二进制数组，其中包含图像数据  [7]：摄像机ID（kTop = 0，kBottom = 1）  [8]：左角（弧度）
            [9]：topAngle（弧度）  [10]：rightAngle（弧度）  [11]：bottomAngle（弧度）"""
        self._videoProxy = ALProxy("ALVideoDevice", _ip, _port)
        self._imgClient = self._videoProxy.subscribeCamera(
            # todo 相机模块测试, 之前订阅模块为: OpenCV_Client, 查找资料探究这个模块有什么作用
            str(rand),  # 所订阅的OpenCV_Client相机, 由于没有使用, 并且一直订阅一个模块会有bug, 所有随机订阅
            self._cameraID,
            self._resolution,
            self._colorSpace,
            self._fps
        )

    # 退订相机
    def _unregister_image_client(self):
        if self._imgClient != "":
            self._videoProxy.unsubscribe(self._imgClient)

    def save_img(self):
        try:
            _imgData = self._videoProxy.getImageRemote(self._imgClient)  # 获取图像, 返回值是存有一张图片的容器
            save_root = r"Y:\work\naoqi_task\pic_datas"
            file_name = str(self.img_file_num) + ".dat"
            with open(os.path.join(save_root, file_name), 'wb') as f:
                pickle.dump(_imgData, f)
            self.img_file_num += 1
            print "save image: ", file_name

        except KeyboardInterrupt:  # 键盘打断
            self._unregister_image_client()  # 退订相机
            print KeyboardInterrupt
            return
        except TypeError:
            print "TypeError"


if __name__ == '__main__':
    # IP = "localhost"
    IP = "192.168.12.104"
    PORT = 9559
    CameraID = 1  # 1下摄像头，0上摄像头
    ALM = ALProxy("ALMotion", IP, PORT)  # NAO的运动对象
    _tts = ALProxy("ALTextToSpeech", IP, PORT)  # NAO的语言对象
    posture = ALProxy("ALRobotPosture", IP, PORT)  # NAO的姿势对象
    # 设置身体姿态
    posture.goToPosture("StandInit", 0.5)  # 半蹲
    ALM.setStiffnesses("Body", 1.0)  # 刚化
    # 锁定头部，让其低头
    ALM.angleInterpolation("HeadPitch", 0.4, 1, False)
    ALM.angleInterpolation("HeadYaw", -0.00, 1, False)
    # stop.setState("disabled")

    myWidget = ClassName(IP, PORT, CameraID, _tts)
    myWidget.img_file_num = 110
    while 1:
        _tts.say("欧了")
        myWidget.save_img()
        time.sleep(1)
