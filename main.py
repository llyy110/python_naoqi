# coding=utf-8
from naoqi import ALProxy

IP = "192.168.1.107"  # 机器人的IP地址
PORT = 9559           # 机器人的端口号，默认9559
ttsProxy = ALProxy("ALTextToSpeech", IP, PORT)


def sayHi():
    ttsProxy.say("你好")


if __name__ == '__main__':
    sayHi()

