# -*- coding: utf-8 -*-
import pickle
from naoqi import ALProxy
import os
import sys
import random
from fastapi

app = FastAPI()

#sdfghnbvc
def get_pic():
    root_path = r"Y:\work\naoqi_task\pic_datas"
    pic_datas_ = os.listdir(root_path)
    file_ = open(os.path.join(root_path, random.choice(pic_datas_)), 'rb')
    return pickle.load(file_, encoding='bytes')


@app.get("/img")
async def img():
    return get_pic()


if __name__ == '__main__':
    # print(get_pic())
    # print(type(get_pic()))

    import uvicorn

    uvicorn.run(app, host="192.168.12.15", port=8001)





IP = "192.168.1.107"  # 机器人的IP地址
PORT = 9559           # 机器人的端口号，默认9559
ttsProxy = ALProxy("ALTextToSpeech", IP, PORT)


def sayHi():
    ttsProxy.say("你好")


if __name__ == '__main__':
    sayHi()

