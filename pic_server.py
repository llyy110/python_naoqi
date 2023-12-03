import fastapi
import pickle
import os
import sys
import random

app = fastapi.FastAPI()

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
